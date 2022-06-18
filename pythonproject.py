import pyttsx3
prps = pyttsx3.init()
def talk(text):
    prps.say(text)
    prps.runAndWait()
print("PRAN-RFL Public School")
talk("PRAN-RFL Public School")
print()
print("Science Fair 2022")
talk("Science Fair 2022")
print()
while True:
    rfl = input("Ask a question : ")
    rfl = rfl.lower()

    if "founded" in rfl:
        if "pran" in rfl:
            if "rfl" in rfl:
                    print("Founder : Major Genarel Amjad Khan Chowdhury")
                    talk("Founder : Major Genarel Amjad Khan Chowdhury")
    elif "ceo" in rfl:
        print("CEO : Ahsan Khan Chowdhury")
        talk("CEO : Ahsan Khan Chowdhury")
    elif "director" in rfl :
        print("Director : Seema Chowdhury")
        talk("Director : Seema Chowdhury")
    elif "advisor" in rfl:
        print("Advisor : Suprita Paul")
        talk("Advisor : Suprita Paul")
    elif "head" in rfl and "hrm" in rfl:
        print("HRM Head is : Faruk hossain")
        talk("HRM Head is : Faruk hossain")
    elif "president" in rfl:
        print("commander M Shamsul alom miah , b an-ob")
        talk("commander M Shamsul alom miah , b an-ob")
    elif "principal" in rfl:
        if "pip" in rfl:
            print("Shah Muhammad: Jewel Reza")
            talk("Shah Muhammad: Jewel Reza")
        elif "hip" in rfl:
            print("Mr.Muhammad Mubinul Hoque Chowdhury")
            talk("Mr.Muhammad Mubinul Hoque Chowdhury")
        elif "danga" in rfl:
            print("Muhammad Shahidur Rahman Khan")
            talk("Muhammad Shahidur Rahman Khan")
        else:
            print("There is no PRAN RFL public school principal in this district")
            talk("There is no PRAN RFL public school principal in this district")
    elif "vice" in rfl and "principal" in rfl:
        if "hip" in rfl:
            print("Muhammad Samsul Islam")
            talk("Muhammad Samsul Islam")
        elif "pip" in rfl:
            print("Muhammad Samsul Islam")
            talk("Muhammad Samsul Islam")
    elif "club" in rfl:
        if "hip" in rfl:
            print("Science Club, Soprts Club, Literary Club, Debate Club")
            talk("Science Club, Soprts Club, Literary Club, Debate Club")
        if "pip" in rfl:
            print("Science Club,Sports Club")
            talk("Science Club, Sports Club")
    elif "sports" in rfl and "teacher" in rfl:
        if "hip" in rfl:
            print("Muhammad Jakir Hossain")
            talk("Muhammad Jakir Hossain")
        if "pip" in rfl:
            print("Muhammad Jakir Hossain")
            talk("Muhammad Jakir Hossain")
    if "science" in rfl :
        if "hip" in rfl :
            print("1 : Chemistry Teacher : Faruk Hossain")
            print("2 : Higher Math Teacher : Mr. Tahazul Islam and Mr.Lutur Rahman")
            print("3 : Physics Teacher : Sarwer Alom")
            print("4 : Bangladesh and Global studies Teacher : Mr. Sanaullah")
            print("5 : Biology Teacher : Mr. Mahfuzur Rahman")
            talk("Chemistry Teacher : Faruk Hossain")
            talk(" Higher Math Teacher : Mr. Tahazul Islam and Mr.Lutur Rahman")
            talk("Physics Teacher : Sarwer Alom")
            talk("Bangladesh and Global studies Teacher : Mr. Sanaullah")
            talk("Biology Teacher : Mr. Mahfuzur Rahman")
        elif "ghorshal" in rfl:
            print("1 : Chemistry Teacher : Masuda Sultana")
            print("2 : Higher Math Teacher : Dipak Chandra Das")
            print("3 : Physics Teacher : Mohaimeen-Bin-Zaman")
            print("4 : Bangladesh and Global studies Teacher : Sumitra Rani Bhowmik")
            print("5 : Biology Teacher : Abu Hanif Sarker")
            print(" Science Teacher : Muhammad Kafi Uddin and Tanzina Sanjid Sinthi")
            talk("1 : Chemistry Teacher : Masuda Sultana")
            talk("2 : Higher Math Teacher : Dipak Chandra Das")
            talk("3 : Physics Teacher : Mohaimeen-Bin-Zaman")
            talk("4 : Bangladesh and Global studies Teacher : Sumitra Rani Bhowmik")
            talk("5 : Biology Teacher : Abu Hanif Sarker")
            talk(" Science Teacher : Muhammad Kafi Uddin and Tanzina Sanjid Sinthi")
        elif "danga" in rfl:
            print("Science Teacher : Sheikh Tahmin Akter Jui")
            talk("Science Teacher : Sheikh Tahmin Akter Jui")
        else:
            print("There is no PRAN RFL public school Science teacher in this district")
            talk("There is no PRAN RFL public school science teacher in this district")
    elif "ict" in rfl :
        if "hip" in rfl:
            print("ICT Teacher : Ms. Shamima Sultana")
            talk("ICT Teacher : Ms. Shamima Sultana")
        elif "pip" in rfl:
            print("ICT Teacher: Muhammad Mosharaf Hossain")
            talk("ICT Teacher : Muhammad Mosharaf Hossain")
        else:
            print("There is no PRAN RFL public school ict teacher in this district")
            talk("There is no PRAN RFL public school ict teacher in this district")
    elif "religion" in rfl :
        if "hip" in rfl:
            print("Islam Teacher : Mr.Abdur Rahman Faruki")
            print("Hindu Teacher : Sharna Bashak")
            talk("Islam Teacher : Mr.Abdur Rahman Faruki")
            talk("Hindu Teacher : Sharna Bashak")
        elif "pip" in rfl:
            print("Islam Teacher : Muhammad Zulfiker Ali")
            print("Hindu Teacher : Shishir Chandra Biswas")
            talk("Islam Teacher : Muhammad Zulfiker Ali")
            talk("Hindu Teacher : Shishir Chandra Biswas")
        else:
            print("There is no PRAN RFL public school religion teacher in this district")
            talk("There is no PRAN RFL public school religion teacher in this district")
    elif "pran" in rfl and "gm" in rfl:
        print("Genarel Manager : Dipak Kumar Dev")
        talk("Genarel Manager : Dipak Kumar Dev")
    elif "incharge" in rfl :
        if "hip" in rfl:
            print("Senior In-charge : Mr. Tahazul Islam")
            print("junior In-charge : Ms. Maksuda Akter Bithi")
            talk("Senior In-charge : Mr. Tahazul Islam")
            talk("junior In-charge : Ms. Maksuda Akter Bithi")
        elif "pip" in rfl:
            print("Junior In-cahrge : Muhammad Mosharaf Hossain")
            talk("Junior In-cahrge : Muhammad Mosharaf Hossain")
        else:
            print("There is no PRAN RFL public school in-charge in this district")
            talk("There is no PRAN RFL public school in-charge in this district")
    elif "bangla" in rfl and "teacher" in rfl:
        if "hip" in rfl :
            print("Bangla Teacher : Mr. Mofakkar Uddin")
            talk("Bangla Teacher : Mr. Mofakkar Uddin")
        elif "pip" in rfl:
            print("Bangla Teacher : Muhammad Tuhidul Islam")
            print(" Bangla Teacher : Muhammad Nur Alam")
            talk("Bangla Teacher : Muhammad Tuhidul Islam")
            talk(" Bangla Teacher : Muhammad Nur Alam")
        elif "danga" in rfl:
            print("Bangla Teacher : Muhammad Shahinur Rahman")
            talk("Bangla Teacher : Muhammad Shahinur Rahman")
        else:
            print("There is no PRAN RFL public school bangla teacher in this district")
            talk("There is no PRAN RFL public school bangla teacher in this district")
    elif "english" in rfl and "teacher" in rfl:
        if "hip" in rfl:
            print("English Teacher : Mr. Biplop Deb")
            print("English Teacher : Ms. Fabiha Chowdhury")
            print("English Teacher : Tahmina Ahsan")
            talk("English Teacher : Mr. Biplop Deb")
            talk("English Teacher : Ms. Fabiha Chowdhury")
            talk("English Teacher : Tahmina Ahsan")
        elif "pip" in rfl:
            print("English Teacher : Subarna mili")
            print("English Teacher : Shayla Ahmed")
            print("English Teacher : Tahmina Sharmin")
            print("English Teacher : Zubayda Sultana")
            talk("English Teacher : Subarna mili")
            talk("English Teacher : Shayla Ahmed")
            talk("English Teacher : Tahmina Sharmin")
            talk("English Teacher : Zubayda Sultana")
        else:
            print("There is no PRAN RFL public school english teacher in this district")
            talk("There is no PRAN RFL public school english teacher in this district")
    elif "commerce" in rfl and "teacher" in rfl:
        if "hip" in rfl :
            print("Finance Banking Teacher : Shamima Aktar Asha")
            print("Accounting Teacher : Dipto Singha ")
            talk("Finance Banking Teacher : Shamima Aktar Asha")
            talk("Accounting Teacher : Dipto Singha ")
        if "pip" in rfl:
            print("Accounting Teacher : Mohammad Kamrul Islam")
            talk("Accounting Teacher : Mohammad Kamrul Islam")
        else:
            print("There is no PRAN RFL public school commerce teacher in this district")
            talk("There is no PRAN RFL public school commerce in this district")
    elif "math" in rfl and "teacher" in rfl:
        if "hip" in rfl :
            print("Math Teacher : Mr. Tahazul Islam ")
            print("Math Teacher : Mr.AKM Abul Bashar Farazi")
            print("Math Teacher : Mr. N.M Ashek Ullah")
            print("Math Teacher : Mr.Lutfur Rahman ")
            print("Math Teacher : Ms. Shaiqun Nahar")
            talk("Math Teacher : Mr. Tahazul Islam ")
            talk("Math Teacher : Mr.AKM Abul Bashar Farazi")
            talk("Math Teacher : Mr. N.M Ashek Ullah")
            talk("Math Teacher : Mr.Lutfur Rahman ")
            talk("Math Teacher : Ms. Shaiqun Nahar")
        elif "pip" in rfl:
            print("Math Teacher : Mazharul Huque")
            print("Math Teacher : Muhammad Aroj Ali")
            print("Math Teacher : Dipak Chandra Das")
            talk("Math Teacher : Mazharul Huque")
            talk("Math Teacher : Muhammad Aroj Ali")
            talk("Math Teacher : Dipak Chandra Das")
        else:
            print("There is no PRAN RFL public school math teacher in this district")
            talk("There is no PRAN RFL public school math teacher in this district")
    elif "junior" in rfl and "teacher" in rfl:
        if "hip" in rfl:
            print("HIP - Junior Section Teachers ")
            talk("hip - Junior section teachers ")
            print("Ms. Apifa Akter")
            print("Ms. Sultana Begum")
            print("Ms. Tahmida Haque ")
            print("Ms. Sirajum Munira tuli")
            print("Ms. Lutfun Nahar Mukti")
            print("Suma Sutradhar Sreya")
            print("Sharna Bashak")
            talk("Ms. Apifa Akter")
            talk("Ms. Sultana Begum")
            talk("Ms. Tahmida Haque ")
            talk("Ms. Sirajum Munira tuli")
            talk("Ms. Lutfun Nahar Mukti")
            talk("Suma Sutradhar Sreya")
            talk("Sharna Bashak")
        elif "pip" in rfl:
            print("PIP - Junior Section Teachers")
            talk("pip - junior section teachers")
            print("Shalma Siddiqua")
            print("Tania Akter Rokeya ")
            print("Ayesha Alieva")
            print("Naznin Nahar")
            print("Farhana Akter")
            print("Shakila Zaman Nipa")
            print("Selina Begum")
            print("Umma Kulsum")
            talk("Shalma Siddiqua")
            talk("Tania Akter Rokeya ")
            talk("Ayesha Alieva")
            talk("Naznin Nahar")
            talk("Farhana Akter")
            talk("Shakila Zaman Nipa")
            talk("Selina Begum")
            talk("Umma Kulsum")
        elif "danga" in rfl :
            print("DANGA - Junior Section Teachers")
            talk("danga - junior section teachers")
            print("Marufa")
            print("Chaitaly Paul")
        else:
            print("There is no PRAN RFL public school junior section teacher in this district")
            talk("There is no PRAN RFL public school junior section teacher in this district")
    elif "admin" in rfl and "officer" in rfl:  
        if "hip" in rfl:
            print("Addmin Officer : Mr. Ajoy Krishna")
            talk("Addmin Officer : Mr. Ajoy Krishna")
        elif "pip" in rfl:
            print("Addmin Oficer : Muhammad Sharif")
            talk("Addmin Officer : Muhammad Sharif")
        elif "danga" in rfl:
            print("Addmin Officer : Tapan Sen")
            talk("Addmin Officer : Tapan Sen")
        else:
            print("There is no PRAN RFL public school addmin officer in this district")
            talk("There is no PRAN RFL public school officer in this district")
    elif "office" in rfl and "assistant" in rfl :
        if "hip" in rfl:
            print("Office Assistant : Shahin Miah")
            print("Office Assistant : Laxmi Rani")
            talk("Office Assistant : Shahin Miah")
            talk("Office Assistant : Laxmi Rani")
        elif "pip" in rfl :
            print("Office Assistant : Muhammad Sohel Miah")
            talk("Office Assistant : Muhammad Sohel miah")
        else:
            print("There is no PRAN RFL public school Office Assistant in this district")
            talk("There is no PRAN RFL public school office Assistant in this district")

    elif "service" in rfl and "assistant" in rfl:
        if "hip" in rfl:
            print("HIP - Service Assistants Name ")
            talk("HIP - Service Assistants Name")
            print("Bilkis")
            print("Fulbashi")
            print("Luki Rani")
            print("Joydeb Rishi")
            talk("Bilkis")
            talk("Fulbashi")
            talk("Luki Rani")
            talk("Joydeb Rishi")
        elif "pip" in rfl:
            print("PIP - Service Assistants Name")
            talk("PIP - Service Assistants Name")
            print("Hajera Begum")
            print("Kohinur Begum")
            print("AL-Amin")
            print("Runa Akter")
            print("Sabiha Begum")
            print("Sathi Akter")
            talk("Hajera Begum")
            talk("Kohinur Begum")
            talk("AL-Amin")
            talk("Runa Akter")
            talk("Sabiha Begum")
            talk("Sathi Akter")
        elif "danga" in rfl :
            print("DANGA - Service Assistants Name")
            talk("Danga - Service Assistants Name")
            print("Mitu Akter")
            print("Sadia")
            print("Shilpi Akter")
            talk("Mitu Akter")
            talk("Sadia")
            talk("Shilpi Akter")
        else:
            print("There is no PRAN RFL public school Service Assistant in this district")
            talk("There is no PRAN RFL public school Service Assistant in this district")
    elif "bus" in rfl :
        if "hip" in rfl:
            print("HIP - Bus Drivers Name")
            talk("HIP - Bus Drivers Name")
            print("Harun Miah")
            print("Muhammad Shahin")
            talk("Harun Miah")
            talk("Muhammad Shahin")
        elif "pip" in rfl:
            print("PIP - Bus Drivers Name")
            talk("HIP - Bus Drivers Name")
            print("Monir Hossain")
            print("Nur Muhammad")
            print("Khondokar Iqbal")
            talk("Monir Hossain")
            talk("Nur Muhammad")
            talk("Khondokar Iqbal")
        else:
            print("There is no PRAN RFL public school Bus Drivers in this district")
            talk("There is no PRAN RFL public school Bus Drivers in this district")
    elif "bus" in rfl and "helper" in rfl:
        if "hip" in rfl:
            print("HIP - Bus Helpers Name")
            talk("HIP - Bus Helpers Name")
            print("Biswajit Rishi")
            print("Abu Sayed")
            talk("Biswajit Rishi")
            talk("Abu Sayed")
        elif "pip"  in rfl:
            print("PIP - Bus Helpers Name")
            talk("PIP - Bus Helpers Name")
            print("Harun Miah")
            print("Kamal Hossain")
            print("Mamun Miah")
            print("Mithu Miah")
            talk("Harun Miah")
            talk("Kamal Hossain")
            talk("Mamun Miah")
            talk("Mithu Miah")
        else:
            print("There is no PRAN RFL public school Bus Helpers in this district")
            talk("There is no PRAN RFL public school Bus Helpers in the district")
    elif "how" in rfl and "many" in rfl and "students" in rfl:
        if "hip" in rfl:
            print("Almost619")
            talk("Almost 619")
        elif "pip" in rfl:
            print("Almost 1300")
            talk("Almost 1300")
        elif "danga" in rfl:
            print("Almost 185")
            talk("Almost 185")
        else:
            print("There is no PRAN RFL public school Students in this district")
            talk("There is no PRAN RFL public school Students in this district")
    elif "how" in rfl and "many" in rfl and "teachers" in rfl:
        if "hip" in rfl:
            print("Almost 32")
            talk("Almost 32")
        elif "pip" in rfl:
            print("Almost 43")
            talk("Almost 43")
        elif "danga" in rfl:
            print("Almost 10")
            talk("Almost 10")
        else:
            print("There is no PRAN RFL public school Teachers in this district")
            talk("There is no PRAN RFL public school Teachers in this district")
    elif "exit" in rfl:
        break
print()
print("Thank you for asking question")
talk("Thank you for asking question")
print()
print("We proud of our school ")
talk("we proud of our school")
print()
print("Here you will find out about PRAN-RFL Public School")
talk("Here you will find out about PRAN-RFL Public School")
print()
print("Project Present by")
talk("Project Present by")
print("Team Name : Albert EinStein")
print("Leader : Ahsanul Mahbub Farhan (Science)")
print("Asisstant Leader : Tanjin Ahmed (Science)") 
print("Asisstant Leader : Ariful Islam Opu (Science)")
print("Asisstant : Nazmus Shakib Muhurto (Science)")
print("Asisstant : Tamim Ahmed (Commerce)")
talk("Team Name : Albert EinStein")
talk("Leader : Ahsanul Mahbub Farhan (Science)")
talk("Asisstant Leader : Tanjin Ahmed (Science)") 
talk("Asisstant Leader : Ariful Islam Opu (Science)")
talk("Asisstant : Nazmus Shakib Muhurto (Science)")
talk("Asisstant : Tamim Ahmed (Commerce)")
