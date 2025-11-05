from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  
  
  path('',views.home2,name="home2"),
  path('about-us/',views.about_us,name ="about-us"),
  path('blog-detail-two/',views.blog_detail_two,name ="blog-detail-two"),
  path('blog-detail/',views.blog_detail,name ="blog-detail"),
  path('blog-grid/',views.blog_grid,name ="blog-grid"),
  path('blog-list/',views.blog_list,name ="blog-list"),
  path('blog-modern/',views.blog_modern,name ="blog-modern"),
  path('blog-standard/',views.blog_standard,name ="blog-standard"),
  path('cart/',views.cart,name ="cart"),
  path('case-studies-detail-two/',views.case_studies_detail_two,name ="case-studies-detail-two"),
  path('case-studies-detail/',views.case_studies_detail,name ="case-studies-detail"),
  path('case-studies-four/',views.case_studies_four,name ="case-studies-four"),
  path('case-studies-three/',views.case_studies_three,name ="case-studies-three"),
  path('case-studies-two/',views.case_studies_two,name ="case-studies-two"),
  path('case-studies-one/',views.case_studies_one,name ="case-studies-one"),
  path('checkout/',views.checkout,name ="checkout"),
  path('contact-us/',views.contact_us,name ="contact-us"),
  path('error-404/',views.error_404,name ="error-404"),
  path('faqs/',views.faqs,name ="faqs"),
  path('index/',views.index,name ="index"),
  path('home3/',views.home3,name ="home3"),
  path('home4/',views.home4,name ="home4"),
  path('home5/',views.home5,name ="home5"),
  path('home6/',views.home6,name ="home6"),
  path('home7/',views.home7,name ="home7"),
  path('list-testimonials/',views.list_testimonials,name ="list-testimonials"),
  path('login/',views.login,name ="login"),
  path('our-team/',views.our_team,name ="our-team"),
  path('pricing-plan/',views.pricing_plan,name ="pricing-plan"),
  path('product-detail/',views.product_detail,name ="product-detail"),
  path('register/',views.register,name ="register"),
  path('service-detail/',views.service_detail,name ="service-detail"),
  path('shop/',views.shop,name ="shop"),
  path('team-detail/',views.team_detail,name ="team-detail"),




  
  
  
  
   ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 