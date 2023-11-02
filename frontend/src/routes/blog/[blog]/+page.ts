import type { PageLoad } from './$types';
import {returnBlog} from "$lib/blog";
import {returnBlogp} from "$lib/blogp";

export const load: PageLoad = ({ params }) => {
	return returnBlog(params.blog) || returnBlogp(params.blog);
};

