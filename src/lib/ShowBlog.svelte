<script lang="ts">
    import {returnBlogp} from "./blogp";
    import {returnBlog} from "$lib/blog";
    let projects = ["onep", "twop", "threep", "fourp", "fivep", "sixp"]
</script>


<div class="flex flex-col items-center " id="project">
    <p class="text-5xl font-bold p-20">Latest Articles</p>

    <!-- Search Category -->
    <div class="join pb-10">
  <div>
    <div>
      <input class="input input-bordered join-item" placeholder="Search"/>
    </div>
  </div>
  <select class="select select-bordered join-item">
    <option disabled selected>Filter</option>
    <option>Lifestyle</option>
    <option>Movie</option>
    <option>Reading</option>
      <option>Fashion</option>
  </select>
  <div class="indicator">
    <button class="btn join-item">Search</button>
  </div>
</div>


    <!-- Category -->
<div class=" pb-10">
<button class="btn  ">Lifestyle</button>
<button class="btn ">Movie</button>
<button class="btn ">Reading</button>
<button class="btn ">Fashion</button>
</div>

        <!-- Blogs -->

    <div class="flex flex-col md:flex-row flex-wrap items-center md:justify-center">
        {#each projects as project }
        <div class="card card-compact w-96 bg-base-100 shadow-xl mx-20 my-10">
          <figure><img src="{returnBlogp(project)?.post.image}" alt="BlogImg" /></figure>
          <div class="card-body">
            <h2 class="card-title">{returnBlogp(project)?.post.title}</h2>
           <div class="card-actions justify-end">
              <a href="/blog/{project}" class="btn btn-primary">Read More</a>
            </div>
          </div>
        </div>
    {/each}
    </div>
    <!-- Page Number -->

    <div class="btn-group pt-5">
  <input type="radio" name="options" data-title="1" class="btn" checked/>
  <input type="radio" name="options" data-title="2" class="btn"  />
  <input type="radio" name="options" data-title="3" class="btn" />
  <input type="radio" name="options" data-title="4" class="btn" />
</div>
</div>