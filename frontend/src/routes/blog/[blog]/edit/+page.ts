import type { PageLoad } from './$types';
import {returnBlog} from "$lib/blog";


export const load: PageLoad = ({ params }) => {
	return returnBlog(params.blog) ;
};

