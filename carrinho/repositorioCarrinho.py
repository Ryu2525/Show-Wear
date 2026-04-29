# from Supabase import supabase

# def inserir_item(user_id, item_id, tipo_item, quantidade, preco_unitario):
#     dados = {
#         "user_id": user_id,
#         "item_id": item_id,
#         "tipo_item": tipo_item,
#         "quantidade": quantidade,
#         "preco_unitario": preco_unitario
#     }
#     return supabase.table("cart_items").insert(dados).execute()

# def buscar_itens(user_id):
#     return supabase.table("cart_items").select("*").eq("user_id", user_id).execute()

# def limpar_carrinho(user_id):
#     return supabase.table("cart_items").delete().eq("user_id", user_id).execute()
