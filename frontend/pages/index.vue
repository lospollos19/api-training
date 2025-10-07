<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <UContainer class="py-12">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold">Bienvenue !</h1>
        <UButton color="red" variant="soft" @click="handleLogout">
          Se déconnecter
        </UButton>
      </div>

      <UCard>
        <p>Ceci est votre page d'accueil protégée. Vous êtes connecté avec l'email : <strong>{{ user?.email }}</strong></p>
        <p class="mt-4">Vous pouvez maintenant commencer à construire le reste de votre application.</p>
      </UCard>
    </UContainer>
  </div>
</template>

<script setup>
// On récupère l'état de l'utilisateur
const user = useState('user');

// Middleware de protection de la page
definePageMeta({
  middleware: ['auth']
})

async function handleLogout() {
  user.value = null; // On déconnecte l'utilisateur
  await navigateTo('/login'); // On le redirige vers la page de login
}
</script>