document.addEventListener('DOMContentLoaded', () => {
    const blogForm = document.getElementById('blogForm');
    const blogsList = document.getElementById('blogsList');
    let editingIndex = null;
    const apiUrl = "http://localhost:8000/blogs"; // Backend API URL

    // Display existing blogs
    async function displayBlogs() {
        try {
            const response = await fetch(apiUrl);
            if (!response.ok) throw new Error("Failed to fetch blogs");
            const blogs = await response.json();
            blogsList.innerHTML = '';
            blogs.forEach((blog) => {
                const blogElement = createBlogElement(blog);
                blogsList.insertBefore(blogElement, blogsList.firstChild);
            });
        } catch (error) {
            console.error("Error fetching blogs:", error);
        }
    }

    // Create blog element
    function createBlogElement(blog) {
        const blogDiv = document.createElement('div');
        blogDiv.className = 'blog-post';
        blogDiv.innerHTML = `
            <h3>${escapeHtml(blog.title)}</h3>
            <div class="date">${new Date(blog.created_at).toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            })}</div>
            <div class="content">${escapeHtml(blog.content)}</div>
            <div class="blog-actions">
                <button class="edit-btn" data-id="${blog.id}">Edit</button>
                <button class="delete-btn" data-id="${blog.id}">Delete</button>
            </div>
        `;

        // Add delete functionality
        const deleteBtn = blogDiv.querySelector('.delete-btn');
        deleteBtn.addEventListener('click', async () => {
            try {
                const response = await fetch(`${apiUrl}/${blog.id}`, {
                    method: 'DELETE'
                });
                if (!response.ok) throw new Error("Failed to delete blog");
                // displayBlogs();
                window.location.reload()
            } catch (error) {
                console.error("Error deleting blog:", error);
            }
        });

        // Add edit functionality
        const editBtn = blogDiv.querySelector('.edit-btn');
        editBtn.addEventListener('click', () => {
            document.getElementById('blogTitle').value = blog.title;
            document.getElementById('blogContent').value = blog.content;
            editingIndex = blog.id;
            document.querySelector('.publish-btn').textContent = 'Update';
            document.querySelector('h2').textContent = 'Edit Post';
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        return blogDiv;
    }

    // Handle form submission
    blogForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const title = document.getElementById('blogTitle').value;
        const content = document.getElementById('blogContent').value;

        if (title.trim() && content.trim()) {
            const blogData = {
                title: title,
                content: content,
                published: true // Default to true
            };

            try {
                if (editingIndex !== null) {
                    // Update existing blog
                    const response = await fetch(`${apiUrl}/${editingIndex}`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(blogData)
                    });
                    if (!response.ok) throw new Error("Failed to update blog");
                    editingIndex = null;
                    document.querySelector('.publish-btn').textContent = 'Publish';
                    document.querySelector('h2').textContent = 'Create New Post';
                } else {
                    // Add new blog
                    const response = await fetch(apiUrl, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify(blogData)
                    });
                    if (!response.ok) throw new Error("Failed to create blog");
                }
                blogForm.reset();
                displayBlogs();
            } catch (error) {
                console.error("Error saving blog:", error);
            }
        }
    });

    // Escape HTML to prevent XSS
    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    // Initial display of blogs
    displayBlogs();
});
