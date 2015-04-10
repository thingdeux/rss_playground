from django.shortcuts import render
from parse.utils import generate_media_details_from_rss, acquire_smallest_images
from django.views.decorators.cache import cache_page


# Cache the page for 24 hours, no need to hit the unchanging RSS feed much
@cache_page(86400)
def display_metadata(request):
    feed = generate_media_details_from_rss(
        'http://www.wdcdn.net/rss/presentation/library/client/iowa/id/128b053b916ea1f7f20233e8a26bc45d')

    smallest_images = acquire_smallest_images(feed)
    return render(request, 'parse/index.html',
        {'feed_items': feed, 'feed_images': smallest_images}
    )