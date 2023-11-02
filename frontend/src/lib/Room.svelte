<script lang="ts">
    import {logged_in} from "$lib/store";
    import {returnBlog} from "./blog";

    let projects = ["one", "two", "three", "four", "five", "six"]
</script>


<div class="flex flex-col items-center " id="project">
    <p class="text-4xl font-bold p-20">Choose a room to book</p>
    <div class="flex flex-col md:flex-row flex-wrap items-center md:justify-center">
        {#each projects as project }
        <div class="card card-compact w-96 bg-base-100 shadow-xl mx-20 my-10">
          <figure><img src="{returnBlog(project)?.post.image}" alt="BlogImg" /></figure>
          <div class="card-body">
            <h2 class="card-title">{returnBlog(project)?.post.title}</h2>
           <div class="card-actions justify-end">
               {#if $logged_in?.role==="admin"}
                     <a href="/blog/{project}" class="btn btn-primary">Edit</a>
                   <a href="/blog/{project}" class="btn btn-primary">Delete</a>
                   {:else}
              <a href="/blog/{project}" class="btn btn-primary">Book Now</a>
                   {/if}
            </div>
          </div>
        </div>
    {/each}
    </div>
</div>