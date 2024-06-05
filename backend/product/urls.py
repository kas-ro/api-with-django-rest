from django.urls import path

from product.views import DetailProductView, CreateProductView, UpdateProductView, DeleteProductView

urlpatterns = [
    # path('', view=views.api_product_view, name="api_product"),
    path('<int:pk>/', view=DetailProductView.as_view()),
    path('create/', view=CreateProductView.as_view()),
    path('<int:pk>/update/', view=UpdateProductView.as_view()),
    path('<int:pk>/delete/', view=DeleteProductView.as_view()),
]
