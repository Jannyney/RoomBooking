<script>
  import { onMount } from 'svelte';

  let formData = {
    first_name: '',
    last_name: '',
    username: '',
    email: '',
    password: '',
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const result = await response.json();
      console.log(result);
    } catch (error) {
      console.error('Error:', error);
    }
  };
</script>

<div class="background h-3/4 " id="get_in_touch">
  <div id="form" class="pb-10">
    <p class="text-neutral text-5xl font-bold p-20 text-center">Sign Up</p>
    <form on:submit|preventDefault={handleSubmit}>
      <div class="min-w-min mb-6">
        <input bind:value={formData.first_name} type="text" name="name" id="name" class="bg-gray-50  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="First Name:" required>
      </div>
      <div class="min-w-min mb-6">
        <input bind:value={formData.last_name} type="text" name="name" id="name" class="bg-gray-50  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Last Name:" required>
      </div>
      <div class="mb-6">
        <input bind:value={formData.username} type="text" name="username" id="username" class="bg-gray-50  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Username:" required>
      </div>
      <div class="mb-6">
        <input bind:value={formData.email} type="email" name="email" id="email" class="bg-gray-50  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Email:" required>
      </div>
      <div class="mb-6">
        <input bind:value={formData.password} type="password" name="subject" id="subject" class="bg-gray-50  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Password:" required>
      </div>
      <div class="mb-6">
        <input type="password" name="subject" id="subject" class="bg-gray-50  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Confirm Password:" required>
      </div>
      <div class="mb-6 flex justify-center">
        <button type="submit" class="btn btn-accent md:max-w-fit text-white  hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center  dark:hover:bg-accent-focus dark:focus:accent-focus" >Sign Up</button>
      </div>
    </form>
  </div>
</div>


<style>
  .background{
    background-color: rgb(255,217,222);
  }
  /*extra small*/
  @media (min-width: 110px) {
    #form {
      margin-left: 1rem;
      margin-right: 1rem;
    }
  }
  /*small*/
  @media (min-width: 640px) {
    #form {
      margin-left: 2.5rem;
      margin-right: 2.5rem;
    }
  }
  /*medium*/
  @media (min-width: 768px){
    #form {
      margin-left: 10rem;
      margin-right: 10rem;
    }
  }
  /*large*/
  @media (min-width: 1024px) {
    #form {
      margin-left: 20rem;
      margin-right: 20rem;
    }
  }
  /*large*/
  @media (min-width: 1536px) {
    #form {
      margin-left: 35rem;
      margin-right: 35rem;
    }
  }
  /*#form {*/
  /*  margin-left: 35rem;*/
  /*  margin-right: 35rem;*/
  /*}*/
</style>
