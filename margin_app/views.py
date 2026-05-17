from django.shortcuts import render


def margin_calculator(request):
    winst = None
    winstmarge = None
    aankoopprijs = None
    verkoopprijs = None

    if request.method == "POST":
        aankoopprijs = float(request.POST.get("aankoopprijs"))
        verkoopprijs = float(request.POST.get("verkoopprijs"))

        winst = verkoopprijs - aankoopprijs

        if verkoopprijs != 0:
            winstmarge = (winst / verkoopprijs) * 100
        else:
            winstmarge = 0

    context = {
        "aankoopprijs": aankoopprijs,
        "verkoopprijs": verkoopprijs,
        "winst": winst,
        "winstmarge": winstmarge,
    }

    return render(request, "margin_app/calculator.html", context)