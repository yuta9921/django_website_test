from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = '太郎'
        return ctxt
    


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["num_services"] = 1500000000
        ctxt["skills"] = [
            "Python",
            "JavaScript",
            "Go",
            "html",
        ] 
        return ctxt

