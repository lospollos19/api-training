// ./frontend/middleware/auth.ts
export default defineNuxtRouteMiddleware((to, from) => {
    // On récupère l'état de l'utilisateur
    const user = useState('user');

    // Si l'utilisateur n'est pas connecté et essaie d'accéder à une autre page que /login
    if (!user.value && to.path !== '/login') {
        // On le redirige vers la page de login
        return navigateTo('/login');
    }
})