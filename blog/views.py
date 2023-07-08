from django.shortcuts import render
from datetime import date
from .models import Author, Post, Tag

# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Maximilian",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Maximilian",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Maximilian",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]


def get_date(post):
    post = Post.objects.all()
    return post

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_detail(request, slug):
    identified_post = Post.objects.get(slug=slug)
    # caption = Post.objects.get(slug)
    return render(request, "blog/post-detail.html", {"post": identified_post, "tags": identified_post.tags.all()})
