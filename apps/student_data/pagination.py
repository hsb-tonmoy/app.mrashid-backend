from rest_framework.pagination import PageNumberPagination


class StudentDataPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        response = super(StudentDataPagination,
                         self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        return response
