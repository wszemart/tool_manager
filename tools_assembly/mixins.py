from django.urls import reverse



class BreadcrumbMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breadcrumbs'] = self.get_breadcrumbs()
        return context

    def get_breadcrumbs(self):
        from .breadcrumb_config import BREADCRUMB_CONFIG
        breadcrumbs = [{'title': 'Strona główna', 'url': reverse('app-home')}]


        view_class = self.__class__

        if view_class in BREADCRUMB_CONFIG:
            for breadcrumb_config in BREADCRUMB_CONFIG[view_class]:
                breadcrumb = breadcrumb_config.copy()

                if callable(breadcrumb['title']):
                    breadcrumb['title'] = breadcrumb['title'](self.object)

                if '{pk}' in breadcrumb['url']:
                    breadcrumb['url'] = breadcrumb['url'].format(pk=self.object.id)

                breadcrumbs.extend(breadcrumb)

        return breadcrumbs
