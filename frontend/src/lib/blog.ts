export function returnBlog(page:string) {
    
    if (page === "one"){

	return {
		post: {
			title: 'Medium-Sized Room',
			image: "https://i.pinimg.com/originals/09/98/70/099870952d9ea7f9b652f98950565789.jpg"
		},
	};
	} else if (page === "two"){

	return {
		post: {
			title: "Conference Room",
			image: "https://images.squarespace-cdn.com/content/v1/59ff781f4c326d235231f58f/1646164693041-3KP9MBP7MTA4L4BELJAF/image-asset.jpeg?format=2500w"
		},
	};
	}

	else if (page === "three"){

	return {
		post: {
			title: "Seminar Room",
			image: "https://event.moc.go.th/file/get/file/20220330ec05a409c5abb7de8d6ae422224a5d29171331.jpg"
		},
	};
	}

	else if (page === "four"){

	return {
		post: {
			title: "Large Conference Room",
			image: "https://e1.pxfuel.com/desktop-wallpaper/893/743/desktop-wallpaper-office-conference-room-meeting-room.jpg"
		},
	};
	}
	else if (page === "five"){

	return {
		post: {
			title: "Green Room",
			image: "https://cdn.shopify.com/s/files/1/0620/6878/5290/files/tf-blog-conference-room-1.jpg?v=1674444600"
		},
	};
	}
	else if (page === "six"){

	return {
		post: {
			title: "Modern Working Room",
			image: "https://www.2010officefurniture.com/wp-content/uploads/2021/11/conference-room-ofs-eleven-conference-table.jpg"
		},
	};
	}

}