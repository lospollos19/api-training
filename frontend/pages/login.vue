<template>
  <!--
    Ce conteneur principal est la clé du centrage :
    - h-screen: prend toute la hauteur de l'écran.
    - flex: active le mode Flexbox.
    - items-center: centre les enfants verticalement.
    - justify-center: centre les enfants horizontalement.
    - p-4: ajoute un peu de marge sur les petits écrans.
  -->
  <div class="h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900 p-4">

    <!--
      UCard est le composant qui crée la "boîte" visible.
      - w-full max-w-sm: la carte prend toute la largeur sur mobile, mais est limitée à une taille raisonnable sur ordinateur.
    -->
    <UCard class="w-full max-w-sm" :ui="{ ring: 'ring-1 ring-gray-200 dark:ring-gray-800' }">
      <template #header>
        <div class="text-center">
          <h1 class="text-3xl font-bold text-gray-900 dark:text-white">
            Connexion
          </h1>
          <p class="mt-1 text-gray-500 dark:text-gray-400">
            Ravi de vous revoir !
          </p>
        </div>
      </template>

      <!-- Le formulaire est maintenant beaucoup plus aéré grâce à `space-y-6` -->
      <UForm :state="state" @submit="handleLogin" class="space-y-6">
        <UFormGroup label="Adresse e-mail" name="email">
          <UInput
              v-model="state.email"
              placeholder="vous@exemple.com"
              icon="i-heroicons-envelope"
              size="xl"
              :ui="{ size: { xl: 'text-lg' } }"
          />
        </UFormGroup>

        <UFormGroup label="Mot de passe" name="password">
          <UInput
              v-model="state.password"
              type="password"
              placeholder="••••••••"
              icon="i-heroicons-lock-closed"
              size="xl"
              :ui="{ size: { xl: 'text-lg' } }"
          />
        </UFormGroup>

        <UButton type="submit" label="Se connecter" color="primary" size="xl" block />
      </UForm>
    </UCard>
  </div>
</template>

<script setup>
const user = useState('user', () => null)

const state = reactive({
  email: '',
  password: ''
})

async function handleLogin() {
  if (state.email && state.password) {
    user.value = { email: state.email };
    await navigateTo('/');
  } else {
    console.error("Veuillez remplir tous les champs.");
  }
}

if (user.value) {
  navigateTo('/');
}
</script>
