from library.feedparser import feedparser
from copy import deepcopy


# Parse a given feed and return a python dictionary with the feed results.
def parse_feed(url):
    if url is not None:
        try:
            result = feedparser.parse(url)
            return result
        except Exception, e:
            print "Unable to parse feed: {}".format(e)
            return False
    else:
        return False


def generate_media_details_from_rss(url):
    result = parse_feed(url)

    if result:
        item_list = result.get('entries', None)

        if item_list is not None:
            # Strip Empty/Null Values from dictionary results (To Include: Empty Strings, 0, Null)
            # I'd prefer stripping the dirty data out at this level rather than on the view. The requirements specified
            # That all metadata should be stored in the dictionary,  an argument could be made for making sure
            # To include empty data in the dictionary irrespective of its value, but I'd like to adhere to mvc
            # standards and keep as much logic out of the view as possible.
            for item in item_list:
                keys_to_remove = []
                temp_dict = deepcopy(item)
                for key, value in temp_dict.iteritems():
                    if key == "media_content":
                        duration = value[0].get('duration', None)
                        vid_type = value[0].get('type', None)
                        if duration is not None:
                            item['duration'] = duration
                        if vid_type is not None:
                            item['compression'] = vid_type

                        # Bitrate options ... I already have the resolution and length
                        # Of the video file, without knowing the audio bitrate calculating may be innacurate.
                        # I don't want to stream it for a short amount of time just to pull metadata from it.
                        # A head request against the content url didn't return enough info to be able to discern.


                    if value == 0 or value == '' or value is None or value == "None":
                        keys_to_remove.append(key)

                for key in keys_to_remove:
                    item.pop(key)
        return item_list


# Iterate over the list of provided thumbnails, find the smallest and create a reference to it for consumption
# by the template
def acquire_smallest_images(item_list):
    thumbnail_dict = {}
    for count, item in enumerate(item_list):
        thumbnail_list = item.get('media_thumbnail', None)
        if thumbnail_list is not None:
            smallest_thumbnail = thumbnail_list[0]
            for image in thumbnail_list:
                if image['height'] < smallest_thumbnail['height']:
                    smallest_thumbnail = image
            # Adding 1 to the count as the forloop django template counter is not 0 indexed.
            thumbnail_dict[count+1] = smallest_thumbnail
        else:
            return False
    return thumbnail_dict