from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import models
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, render_to_response
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from website.forms import *
from django.contrib.auth.models import User
from website.models import *
from django.shortcuts import render, get_object_or_404

def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            loguser=request.user
            userprofile = profile.objects.get(username=loguser)
            userwallet = wallet.objects.get(owner=loguser)
            if userprofile.count==0:
                return redirect('/dashboardedit/')

            return render(request, 'website/home.html',{ 'user' : user , 'profile' : userprofile, 'wallet' : userwallet })
        # Redirect to a success page.
        else:
            return render(request,"website/login.html",{ 'message': 'true'})


    else:
        if not request.user.is_authenticated:
            return redirect('/login/')
        else:
            loguser = request.user
            userprofile = profile.objects.get(username=loguser)
            userwallet = wallet.objects.get(owner=loguser)
            if userprofile.count == 0:
                return redirect('/dashboardedit/')

            return render(request, 'website/home.html', {'user': request.user, 'profile': userprofile, 'wallet': userwallet})


def logout1(request):
    logout(request)
    request.session['emailid']=''
    request.session['user']=''
    return render(request, 'website/logout.html')

def emailconfirm(request):
    if request.method == "POST":
        ema=request.POST['email']
        request.session['emailid'] = ema

        if(User.objects.filter(email=ema).exists()):
            return render(request, "website/reset.html", {'email': ema})
        else:
            return render(request, 'website/forgot-password.html',{ 'message': 'true'})
    else:
        return render(request, 'website/forgot-password.html',{ 'message': 'false'})


def resetpass(request):
    if request.method == "POST":
        ema = request.session.get('emailid')
        user = User.objects.get(email=ema)

        data = {'new_password1': request.POST['password'],
                'new_password2': request.POST['password2']}
        form = SetPasswordForm(user, data)
        if form.is_valid():
            form.save()
            return render(request, "website/login.html", {'message': 'password'})
        else: return render(request, 'website/reset.html')
    else:
        return render(request, 'website/reset.html')


def signup1(request):
    if request.method == 'POST':
        ema= request.POST['email']
        use=request.POST['username']
        data = {'username': request.POST['username'], 'email': request.POST['email'],
                'password1': request.POST['password1'],
                'password2': request.POST['password2']}
        if (User.objects.filter(email=ema).exists()):
            return render(request, 'website/signup.html', {'message': 'email already exists'})
        if (User.objects.filter(username=use).exists()):
            return render(request, 'website/signup.html', {'message': 'username already exists'})


        print(data)
        form = SignUpForm(data)


        if form.is_valid():
            form.save()
            user_in= User.objects.get(email=ema)
            userprofile= profile.objects.create(username=user_in,count=0)
            userwallet=wallet.objects.create(owner=user_in,amount=0)
            usercart=Cart.objects.create(user=user_in)
            userprofile.save()
            userwallet.save()
            usercart.save()


            return render(request, "website/login.html", {'message': 'signed'})
        else:
             return render(request, 'website/signup.html')
    else:

        return render(request, 'website/signup.html')

def dashboard(request):
    if request.method == 'POST':
        loguser = request.user
        use = profile.objects.get(username=loguser)
        use.name=request.POST['name']
        use.address=request.POST['address']
        use.dob=request.POST['dob']
        use.phone=request.POST['phone']
        use.country=request.POST['country']
        use.count=1
        use.account="QT"+use.phone


        #data = {'name': request.POST['name'],'address': request.POST['address'], 'dob': request.POST['dob'],
         #       'phone': request.POST['phone'],'country': request.POST['country']}
        #print(data)
        #form = DashboardForm(data)


        use.save()
        return redirect('/home/')

    else:
        loguser = request.user
        use = profile.objects.get(username=loguser)
        return render(request, 'website/dash.html',{ 'user' : use })

def dashboard1(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            loguser = request.user
            use = profile.objects.get(username=loguser)
            use.name = request.POST['name']
            use.address = request.POST['address']
            use.dob = request.POST['dob']
            use.phone = request.POST['phone']
            use.country = request.POST['country']

            use.save()
            return redirect('/home/')

        else:
            loguser = request.user
            use = User.objects.get(username=loguser)
            pro = profile.objects.get(username=loguser)
            return render(request, 'website/dash2.html', {'user': use , 'pro':pro})


def wallet1(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:

        loguser = request.user
        userprofile = profile.objects.get(username=loguser)
        userwallet = wallet.objects.get(owner=loguser)
        return render(request, 'website/wallet.html', {'user': loguser, 'profile': userprofile, 'wallet': userwallet})


def addmoney(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        loguser = request.user
        userprofile = profile.objects.get(username=loguser)
        userwallet = wallet.objects.get(owner=loguser)
        if request.method == 'POST':

            return render(request, 'website/confirmpay.html', {'user': loguser, 'profile': userprofile, 'wallet': userwallet})
        else:
            return render(request, 'website/payment.html',
                          {'user': loguser, 'profile': userprofile, 'wallet': userwallet})


def payselect(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        return render(request,'website/payselect.html')



def netbank(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            amo=request.POST['amount']
            loginid=request.POST['loginid']
            password=request.POST['password']
            if (bankaccount.objects.filter(username=loginid).exists()):
                a=bankaccount.objects.get(username=loginid)
                loguser = request.user
                userprofile = profile.objects.get(username=loguser)
                userwallet = wallet.objects.get(owner=loguser)

                if password==a.password:
                    if a.amount>=int(amo):
                        a.amount=a.amount-int(amo)


                        a.save()
                        if request.session['cash']:
                            userwallet.amount = 0
                            userwallet.save()

                        message="all items bought successfully"
                        request.session['cost'] = 0
                        request.session['cash'] = 0
                        return render(request, 'website/home.html',
                                  {'user': loguser, 'profile': userprofile, 'wallet': userwallet,'message':message})
                    else:
                        message = "Insufficient balance"
                        addmon = request.session.get('cost')
                        return render(request, 'website/cartpay.html',
                                      {'user': loguser, 'profile': userprofile, 'wallet': userwallet,
                                       'message': message})

                else:
                    addmon = request.session.get('cost')
                    message = "wrong password"
                    return render(request, 'website/netbanking1.html', {'message': message,'addmon':addmon })
            else:
                addmon = request.session.get('cost')
                message="enter valid account details"
                return render(request, 'website/netbanking1.html', {'message': message,'addmon':addmon})




        else:
            if request.session.get('cost'):
                addmon=request.session.get('cost')
            else:
                addmon=0
            return render(request, 'website/netbanking1.html' ,{'addmon':addmon})

def netbankmain(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            amo=request.POST['amount']
            loginid=request.POST['loginid']
            password=request.POST['password']
            if (bankaccount.objects.filter(username=loginid).exists()):
                a=bankaccount.objects.get(username=loginid)
                loguser = request.user
                userprofile = profile.objects.get(username=loguser)
                userwallet = wallet.objects.get(owner=loguser)

                if password==a.password:
                    if a.amount>=int(amo):
                        a.amount=a.amount-int(amo)
                        userwallet.amount = userwallet.amount + int(amo)

                        a.save()
                        userwallet.save()
                        message="successful transaction"
                        request.session['cost'] = 0
                        request.session['cash'] = 0
                        return render(request, 'website/home.html',
                                  {'user': loguser, 'profile': userprofile, 'wallet': userwallet,'message':message})
                    else:
                        message = "Insufficient balance"
                        return render(request, 'website/cartpay.html',
                                      {'user': loguser, 'profile': userprofile, 'wallet': userwallet,
                                       'message': message})

                else:
                    message = "wrong password"
                    return render(request, 'website/netbanking.html', {'message': message })
            else:
                message="enter valid account details"
                return render(request, 'website/netbanking.html', {'message': message})




        else:

            addmon=0
            return render(request, 'website/netbanking.html' ,{'addmon':addmon})






'''def displaybalance(request):
    data = wallet.objects.all();
    return render(request, 'website/wallet.html' ,{ "data":data })

def transac(request):
    if request.method == 'POST':
        data = {'sender': request.POST['sender'],'receiver': request.POST['receiver'], 'desc': request.POST['desc'],
                'date': request.POST['date'],'amount': request.POST['amount']}
        print(data)
        form = TransacForm(data)


        if form.is_valid():
            form.save()
            return redirect('/wallet/')
        else:

            return render(request, 'website/transac.html',{ 'message': 'invalid transaction'})
    else:

        return render(request, 'website/transac.html')'''


'''def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'website/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'website/detail.html', context)'''


def cart_list(request):
    data = item.objects.all()
    return render(request, 'website/cart.html' ,{ "data":data })


def conf(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            loguser=request.user
            cart=Cart.objects.get(user=loguser)
            cart.i1c=request.POST['i1c']
            cart.i2c = request.POST['i2c']
            cart.i3c = request.POST['i3c']
            cart.i4c = request.POST['i4c']
            cart.i5c = request.POST['i5c']
            cart.i6c = request.POST['i6c']
            cart.q1c = request.POST['q1c']
            cart.q2c = request.POST['q2c']
            cart.q3c = request.POST['q3c']
            cart.q4c = request.POST['q4c']
            cart.q5c = request.POST['q5c']
            cart.q6c = request.POST['q6c']

            cart.save()
            item1 = item.objects.get(Name='Toy1')
            item2 = item.objects.get(Name='Toy2')
            item3 = item.objects.get(Name='Toy3')
            item4 = item.objects.get(Name='Toy4')
            item5 = item.objects.get(Name='Toy5')
            item6 = item.objects.get(Name='Toy6')
            cost = 0
            print("lolololololol",int(cart.q1c))
            if (cart.i1c=='True'):
                  cost = cost+int(item1.Cost)*int(cart.q1c)
            if (cart.i2c=='True'):
                cost = cost+int(item2.Cost)*int(cart.q2c)
            if (cart.i3c=='True'):
                cost = cost+int(item3.Cost)*int(cart.q3c)
            if (cart.i4c=='True'):
                cost = cost+int(item4.Cost)*int(cart.q4c)
            if (cart.i5c=='True'):
                cost = cost+int(item5.Cost)*int(cart.q5c)
            if (cart.i6c=='True'):
                cost = cost+int(item6.Cost)*int(cart.q6c)

            request.session['cost']= cost
            request.session['cash'] = cost

            return render(request,"website/cartpay.html",{'cash':cost})     #specify the payment page here
        else:
            item1 = item.objects.get(Name='Toy1')
            item2 = item.objects.get(Name='Toy2')
            item3 = item.objects.get(Name='Toy3')
            item4 = item.objects.get(Name='Toy4')
            item5 = item.objects.get(Name='Toy5')
            item6 = item.objects.get(Name='Toy6')
            data = item.objects.all()
            return render(request, 'website/cart1.html' ,{ "data":data , "item1":item1, "item2":item2,"item3":item3,"item4":item4,"item5":item5,"item6":item6})





def card(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        sampcard = list(savedcards.objects.filter(ownername=request.user))
        count=savedcards.objects.filter(ownername=request.user).count()

        return render(request, 'website/card.html',{'sav' : sampcard ,'count': range(count) })

def card1(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        sampcard = list(savedcards.objects.filter(ownername=request.user))
        count=savedcards.objects.filter(ownername=request.user).count()

        return render(request, 'website/card1.html',{'sav' : sampcard ,'count': range(count) })


def cardpass(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            addmon=request.session.get('addmon')
            cardnumber = request.session.get('cardnumber')
            card=savedcards.objects.get(number=cardnumber)
            card.password=request.POST['password']
            loguser = request.user
            userprofile = profile.objects.get(username=loguser)
            userwallet = wallet.objects.get(owner=loguser)
            if card.amount>=int(addmon):
                card.amount=card.amount-int(addmon)
                userwallet.amount = userwallet.amount + int(addmon)
                card.save()
                userwallet.save()
                message="money addition success"
                request.session['cost'] = 0
                request.session['cash'] = 0
                return render(request, 'website/home.html',
                              {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'message': message})
            else:
                message="password set succesfully but insufficient funds"
                return render(request, 'website/wallet.html',
                              {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'message': message})

        else:

            return render(request, 'website/cardpassset.html')

def cardpass1(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            addmon=request.session.get('addmon')
            cardnumber = request.session.get('cardnumber')
            card=savedcards.objects.get(number=cardnumber)
            card.password=request.POST['password']
            loguser = request.user
            userprofile = profile.objects.get(username=loguser)
            userwallet = wallet.objects.get(owner=loguser)
            if card.amount>=int(addmon):
                card.amount=card.amount-int(addmon)
                card.save()
                if request.session['cash']:
                    userwallet.amount = 0
                    userwallet.save()

                message="all items bought successfuly"
                request.session['cost'] = 0
                request.session['cash'] = 0
                return render(request, 'website/home.html',
                              {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'message': message})
            else:
                message="password set succesfully but insufficient funds"
                return render(request, 'website/cartpay.html',
                              {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'message': message})

        else:

            return render(request, 'website/cardpassset1.html')




def payment(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            loguser=request.user

            sampcard=savedcards.objects.create(ownername=loguser)
            sampcard.name=request.POST['name']
            sampcard.number=request.POST['cardnumber']
            sampcard.cvv=request.POST['cvv']
            sampcard.month=request.POST['expmonth']
            sampcard.year=request.POST['expyear']
            sampcard.save()
            request.session['addmon'] = request.POST['amount']
            request.session['cardnumber'] = request.POST['cardnumber']
            return render(request, 'website/cardpassset.html')



        else:
            if request.session.get('cost'):
                addmon=request.session.get('cost')
            else:
                addmon=0
            return render(request, 'website/payment.html' ,{'addmon':addmon})

def payment1(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            loguser=request.user

            sampcard=savedcards.objects.create(ownername=loguser)
            sampcard.name=request.POST['name']
            sampcard.number=request.POST['cardnumber']
            sampcard.cvv=request.POST['cvv']
            sampcard.month=request.POST['expmonth']
            sampcard.year=request.POST['expyear']
            sampcard.save()
            request.session['addmon'] = request.POST['amount']
            request.session['cardnumber'] = request.POST['cardnumber']
            return render(request, 'website/cardpassset1.html')



        else:
            if request.session.get('cost'):
                addmon=request.session.get('cost')
            else:
                addmon=0
            return render(request, 'website/payment1.html' ,{'addmon':addmon})




def cardselect(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        addmon = request.session.get('cost')
        if request.method == 'POST':
            loguser=request.user
            password=request.POST['password']
            amount=request.POST['amo']
            sampcard = list(savedcards.objects.filter(ownername=request.user))
            val=request.session['val']
            val=int(val)
            if sampcard[val-1].password == password:
                loguser = request.user
                userprofile = profile.objects.get(username=loguser)
                userwallet = wallet.objects.get(owner=loguser)
                if sampcard[val-1].amount >= int(amount):
                    sampcard[val-1].amount = sampcard[val-1].amount - int(amount)
                    userwallet.amount = userwallet.amount + int(amount)
                    userwallet.save()
                    sampcard[val-1].save()
                    message="successful transaction"
                    request.session['cost'] = 0
                    request.session['cash'] = 0
                    return render(request, 'website/home.html', {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'message': message})
                else:
                    message="insufficient funds! try other methods"
                    return render(request, 'website/payselect.html', {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'message': message})
            else:
                message="wrong password"
                return render(request, 'website/cardpay.html', {'message':message,'addmon':addmon})
        else:
            request.session['val']=request.GET['card']

            return render(request, 'website/cardpay.html',{'addmon':addmon})




def cardselect1(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        addmon = request.session.get('cost')
        if request.method == 'POST':
            loguser=request.user
            password=request.POST['password']
            amount=request.POST['amo']
            sampcard = list(savedcards.objects.filter(ownername=request.user))
            val=request.session['val']
            val=int(val)
            if sampcard[val-1].password == password:
                loguser = request.user
                userprofile = profile.objects.get(username=loguser)
                userwallet = wallet.objects.get(owner=loguser)
                if sampcard[val-1].amount >= int(amount):
                    sampcard[val-1].amount = sampcard[val-1].amount - int(amount)

                    sampcard[val-1].save()
                    if request.session['cash'] :
                        userwallet.amount=0
                        userwallet.save()

                    message="items have been succesfully bought"
                    request.session['cost'] = 0
                    request.session['cash'] = 0
                    return render(request, 'website/home.html', {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'message': message})
                else:
                    message="insufficient funds! try other methods"
                    return render(request, 'website/cartpay1.html', {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'message': message})
            else:
                message="wrong password"
                return render(request, 'website/cardpay1.html', {'message':message,'addmon':addmon})
        else:
            request.session['val']=request.GET['card']

            return render(request, 'website/cardpay1.html',{'addmon':addmon})







def cartpay(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        loguser = request.user
        userprofile = profile.objects.get(username=loguser)
        userwallet = wallet.objects.get(owner=loguser)
        return render(request, 'website/cartpay.html',{'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'cash':request.session['cost']})

def walletpay(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    else:
        loguser = request.user
        userprofile = profile.objects.get(username=loguser)
        userwallet = wallet.objects.get(owner=loguser)
        cash = request.session['cash']
        if request.method == 'POST':


            if userwallet.amount>=int(cash):
                userwallet.amount=userwallet.amount-int(cash)
                userwallet.save()
                message="successfully bought the items"
                request.session['cost'] = 0
                request.session['cash'] = 0

                return render(request, 'website/cart1.html', {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'cash': cash, 'message': message })
            else:
                addmon=int(cash)-userwallet.amount

                request.session['cost'] = addmon
                return render(request, 'website/paywalletselect.html',
                              {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'cash': cash,
                               'addmon': addmon})
        else:
            return render(request, 'website/walletpay.html',
                          {'user': loguser, 'profile': userprofile, 'wallet': userwallet, 'cash': cash,
                           })


def tbook(request):
    if request.method == 'POST':
        loguser = request.user
        mn = request.POST['moviename']
        
        ms = request.POST['seats']
        mv = Movie.objects.get(name=mn)

        tc = int(ms)*int(mv.cost)
        mb = TicketBook.objects.create(user=loguser,seats=int(ms),movie=Movie.objects.get(name=mn),amount = tc)
        mb.save()
        print("total cost",tc)
        request.session['bookingtotal'] = tc
        request.session['cost'] = tc
        request.session['cash'] = tc

        return render(request, "website/cartpay.html", {'cash': tc})

    else:
        data = Movie.objects.all()
        return render(request, 'website/tbook.html',{'data': data})    
        

def btbook(request):
    if request.method == 'POST':
        loguser = request.user
        mn = request.POST['busname']
        ms = request.POST['seats']
        mv = Bus.objects.get(name=mn)
        tc = int(ms)*int(mv.cost)
        mb = TicketBookBus.objects.create(user=loguser,bus=Bus.objects.get(name=mn),seats=int(ms),amount = tc)
        mb.save()
        print(mb)
        request.session['bookingtotal'] = tc
        request.session['cost'] = tc
        request.session['cash'] = tc

        return render(request, "website/cartpay.html", {'cash': tc})

    else:
        data = Bus.objects.all()
        return render(request, 'website/btbook.html',{'data':data})    


def bpay(request):
    if request.method == 'POST':
        loguser = request.user
        mn = request.POST['phone']
        bo = Bill.objects.get(phone=mn)
        request.session['eletot']=bo.amount
        return redirect('/promo/')
    else:
        return render(request, 'website/bp.html')

def promo(request):
    if request.method == 'POST':
        loguser = request.user
        ic = request.session['eletot']
        mn = request.POST['name']
        bo = Promo.objects.get(name=mn)
        finalcost = ((100-bo.perc)*ic)/100
        print("final cost:- ",finalcost)
        request.session['eletot']=finalcost
        request.session['cost'] = finalcost
        request.session['cash'] = finalcost

        return render(request, "website/cartpay.html", {'cash': finalcost})
    else:
        tc = request.session['eletot']
        data = Promo.objects.all()
        return render(request, 'website/promo.html',{'tc':tc, 'data':data})

def shopping(request):
    loguser = request.user
    userprofile = profile.objects.get(username=loguser)
    userwallet = wallet.objects.get(owner=loguser)
    if request.method == 'POST':

        amount = request.POST['total']

        request.session['cost'] = amount
        request.session['cash'] = amount

        return render(request, "website/cartpay.html", {'cash': amount})
    else:
        return render(request, 'website/shopping.html', {'user': loguser, 'profile': userprofile, 'wallet': userwallet})
