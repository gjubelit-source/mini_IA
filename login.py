#login con decorador 
def require_auth(func):
    def wrapper(user):
        if user.lower() == "administrador":
            return func(user) 
        else:
            return "Acceso denegado"
    return wrapper


@require_auth
def admin_dashboard(user):
    return f"Bienvenido al panel, {user}"


print(admin_dashboard("Administrador"))
print(admin_dashboard("Super administrador"))