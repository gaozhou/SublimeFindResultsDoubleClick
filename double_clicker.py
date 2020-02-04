import sublime, sublime_plugin

class DoubleClickAtCaretCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        view = self.view
        for idx, vector in enumerate(map(lambda sel: view.text_to_window(sel.begin()), view.sel())):
            view.run_command('drag_select', {
                'event': {
                    'button': 1,
                    'count': 2,
                    'x': vector[0],
                    'y': vector[1]
                },
                'by': 'words',
                'additive': idx > 0 or kwargs.get('additive', False)
            })