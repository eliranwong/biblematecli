def extract_bible_references(event=None):
    from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
    
    buffer = event.app.current_buffer if event is not None else text_field.buffer
    selectedText = buffer.copy_selection().text
    references = BibleVerseParser(False).extractAllReferencesReadable(selectedText)
    buffer.insert_text(format_assistant_content(references))
    get_app().reset()
