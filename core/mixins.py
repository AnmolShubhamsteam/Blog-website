from django.http import HttpResponseForbidden

class UserIsOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            return HttpResponseForbidden("You are not allowed to edit or delete this post.")
        return super().dispatch(request, *args, **kwargs)