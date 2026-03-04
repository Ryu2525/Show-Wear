from supabase import create_client, Client

url: str = "https://frqlowmyzyhacwyxukxw.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZycWxvd215enloYWN3eXh1a3h3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1NjM2NDUsImV4cCI6MjA4ODEzOTY0NX0.fHhePOQoI7teZKNteFwvKj7A51fTsK9vt4FNwHW9suY"
supabase: Client = create_client(url, key)

def criar_usuario(email, senha):
    try:
        # Tenta inserir na tabela 'clientes'
        dados = {"email": email, "senha": senha}
        response = supabase.table("clientes").insert(dados).execute()
        return True, "Usuário cadastrado com sucesso!"
    except Exception as e:
        # Se o e-mail já existir (erro de UNIQUE), o Supabase avisará aqui
        return False, f"Erro ao cadastrar: {str(e)}"

def verificar_login(email, senha):
    try:
        # Busca o usuário pelo e-mail e senha
        response = supabase.table("clientes").select("*").eq("email", email).eq("senha", senha).execute()
        if len(response.data) > 0:
            return True, response.data[0]
        else:
            return False, "E-mail ou senha incorretos."
    except Exception as e:
        return False, f"Erro na conexão: {str(e)}"