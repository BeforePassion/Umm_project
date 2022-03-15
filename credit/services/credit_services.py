def my_point(request):
    point = request.user.point
    return HttpResponse(point)



def charge(request, point):
    p = request.user.point
    UserModel.objects.filter(id=request.user.id).update(point=p+int(point))
    PointHistory.objects.create(user_id=request.user.id, point=int(point), history='charge', usage=True)
    return redirect('/point')



def charge_history(request, page: int):
    data = PointHistory.objects.filter(user_id=request.user.id, usage=True)
    data = list(data.values())
    p = Paginator(data, 5)
    total_page = p.num_pages
    p_data = p.page(page)
    p_data = p_data.object_list
    t_page = {"total_page": total_page}
    data = {"p": p_data, "t": t_page}

    return JsonResponse(data, safe=False)



def usage_history(request):
    data = PointHistory.objects.filter(user_id=request.user.id, usage=False)
    data = list(data.values())
    return JsonResponse(data, safe=False)
