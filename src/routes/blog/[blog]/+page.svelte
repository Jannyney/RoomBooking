<script lang="ts">
	import type { PageData } from './$types';

	export let data: PageData;
</script>
{ #if data.post}
    <img style="width: 40%; display: block; margin-left: auto; margin-right: auto;" src="{data.post.image}" alt="Room Image">
    <h1 class="font-bold text-5xl text-center py-10">{data?.post.title}</h1>
    <div class="text-center text-justify px-56 pt-10 pb-20 text-xl" style="white-space: pre-wrap">{ data?.post.content}</div>

    <div class="flex flex-col items-center pb-10">
        <p class="text-neutral text-4xl font-bold pb-10 text-center">Comment</p>

    <div class="rating rating-lg ">
  <input type="radio" name="rating-9" class="rating-hidden" />
  <input type="radio" name="rating-9" class="mask mask-star-2" />
  <input type="radio" name="rating-9" class="mask mask-star-2"  />
  <input type="radio" name="rating-9" class="mask mask-star-2" />
  <input type="radio" name="rating-9" class="mask mask-star-2" checked/>
  <input type="radio" name="rating-9" class="mask mask-star-2" />
</div></div>

    <div  id="form">
  <form>
      <div class="min-w-min mb-6">
        <input type="text" name="name" id="name" class="bg-neutral-content  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Name: " required>
      </div>
     <div class="mb-6">
        <textarea id="message" name="message" rows="4" class="bg-neutral-content  text-sm rounded-lg  block w-full p-2.5  dark:text-black " placeholder="Message: "></textarea>
      </div>

      <div class="mb-6 flex justify-center">
        <button type="submit" class="btn btn-accent md:max-w-fit text-white  hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center  dark:hover:bg-accent-focus dark:focus:accent-focus">Post</button>
      </div>
    </form>
    </div>

    <style>

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
{/if}