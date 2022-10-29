queue = {}


def queue_audio(chat_id, details):
    in_queue = len(queue[chat_id])
    next = in_queue + 1
    queue[chat_id][in_queue] = details

def queue_video(chat_id, details):
    in_queue = len(queue[chat_id])
    next = in_queue + 1
    queue[chat_id][in_queue] = details

    
