from supabase import create_client, Client

url: str = "https://frqlowmyzyhacwyxukxw.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZycWxvd215enloYWN3eXh1a3h3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1NjM2NDUsImV4cCI6MjA4ODEzOTY0NX0.fHhePOQoI7teZKNteFwvKj7A51fTsK9vt4FNwHW9suY" # Use a chave que você postou
supabase: Client = create_client(url, key)

def cadastrarUsuario(email, senha):
    try:
        dados = {"email": email, "senha": senha}
        supabase.table("clientes").insert(dados).execute()
        return True, "Usuário cadastrado com sucesso!"
    except Exception as e:
        return False, f"Erro ao cadastrar: {str(e)}"

def  realizarLogin(email, senha):
    try:
        response = supabase.table("clientes").select("*").eq("email", email).eq("senha", senha).execute()
        if len(response.data) > 0:
            return True, response.data[0]
        else:
            return False, "E-mail ou senha incorretos."
    except Exception as e:
        return False, f"Erro na conexão: {str(e)}"

# --- FUNÇÕES PARA O CATÁLOGO ---

def  buscarShowsAtivos():
    try:
        response = supabase.table("show").select("*").execute()
        return response.data
    except Exception as e:
        return []

def buscarVestuarioTematico(show_id):
    try:
        response = supabase.table("vestuarios").select("*").eq("show_id", show_id).execute()
        return response.data
    except Exception as e:
        return []

def buscar_ingressos_por_show(show_id):
    try:
        response = supabase.table("ingressos").select("*").eq("show_id", show_id).execute()
        return response.data
    except Exception as e:
        print(f"Erro: {e}")
        return []

def verificarDisponibilidade(vestuario_id):
    try:
        response = supabase.table("vestuarios").select("status, nome_peca").eq("id", vestuario_id).execute()
        
        if response.data:
            item = response.data[0]
            status = item.get("status", "").lower()
            
            if status == "disponível":
                return True, f"O produto '{item['nome_peca']}' está disponível!"
            else:
                return False, f"O produto '{item['nome_peca']}' não está disponível no momento (Status: {status})."
        else:
            return False, "Produto não encontrado."
            
    except Exception as e:
        return False, f"Erro ao verificar disponibilidade: {str(e)}"