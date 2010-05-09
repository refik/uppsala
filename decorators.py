class rendered_with(object):
    def __init__(self, template_name):
        self.template_name = template_name

    def __call__(self, func):
        def rendered_func(request, *args, **kwargs):
            items = func(request, *args, **kwargs)
            return render_to_response(self.template_name, items, context_instance=RequestContext(request))

        return rendered_func
