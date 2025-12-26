from core.views import BaseReadOnlyViewSet
from groups.filters import GroupMemberFilterSet
from apps.groups.models import GroupMember
from groups.serializers import GroupMemberSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


class GroupMemberPagination(PageNumberPagination):
    page_size = 24


class GroupMemberViewSet(BaseReadOnlyViewSet):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    pagination_class = GroupMemberPagination
    filterset_class = GroupMemberFilterSet

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs != {}:
            if "group_pk" in self.kwargs:
                queryset = queryset.filter(group__pk=self.kwargs["group_pk"])
        return queryset

    # def list(self, request, group_pk=None):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     return self.paginated_response(queryset, context={'request': request})
