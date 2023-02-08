from django.shortcuts import render


# def myprofile(request):
#     return render(request, 'myprofile.html')

# def about(request):
#     data = """
#         Lorem ipsum dolor sit amet consectetur adipisicing elit. 
#         Aliquam qui hic corrupti illum itaque. Laudantium cupiditate         
#         necessitatibus voluptates qui provident ipsa fuga odit! Esse 
#         iste enim illo nemo, ratione libero vitae atque sunt, fuga minima 
#         aut. Mollitia, magni sed, maxime molestiae vel voluptate repellendus 
#         blanditiis laudantium assumenda accusantium accusamus in consectetur 
#         sapiente exercitationem! Numquam consequatur enim officiis sint inventore
#          totam repellendus nemo facilis aliquid, ad quae saepe, earum exercitationem 
#          odit iure fugit illum itaque natus in? Rem labore ratione iste, molestiae ex
#           consequatur tenetur tempora expedita atque impedit aliquid quas magnam commodi 
#           alias in similique praesentium exercitationem. Dolores, consequatur pariatur.
#     """
#     return render(request, 'about.html', {"data":data})


def base(request):
    return render(request,'base.html')