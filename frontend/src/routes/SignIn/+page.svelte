<script lang="ts">
import {logged_in} from "$lib/store";
  import {goto} from "$app/navigation";
  let username = "";
  let password = "";

async function save() {
        const myHeaders = new Headers();
        myHeaders.append("Origin", "");
        myHeaders.append("accept", 'application/json');
        myHeaders.append("Content-Type", 'application/json');
        // console.log($page.params.id)
        await fetch(`http://localhost:8000/login`,
            {
                headers: myHeaders,
                method: "POST",
                body: JSON.stringify({
                    'username': username,
                  'password':password
                })
            }

        ).then(res => res.json()).then(data => logged_in.set(data)).then(() => {
            goto("/")
        })
    }

</script>

<div class="background h-3/4 pt-10 pb-52" id="get_in_touch">
  <div id="form" class="pb-10 ">
    <p class="text-neutral text-5xl font-bold p-20 text-center">Log In</p>
    <form>
      <div class="min-w-min mb-6">
        <input bind:value={username} type="text" name="name" id="name" class="bg-gray-50  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Username: " required>
      </div>
      <div class="mb-6">
        <input bind:value={password} type="password" name="email" id="email" class="bg-gray-50  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Password: "required>
      </div>

      <div class="mb-6 flex justify-center">
        <button on:click={save}  class="btn btn-accent md:max-w-fit text-white  hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center  dark:hover:bg-accent-focus dark:focus:accent-focus">Log In</button>
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
