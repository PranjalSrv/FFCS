import demjson

d = {}
f = -1
r = -1


def delete (selectedCourses,selectedSlots):
    srno = 1
    delCourse = []
    delCourseTitles = []
    for i in selectedCourses:
        if i['TITLE'] not in delCourseTitles:
            delCourse.append(i)
            delCourseTitles.append(i['TITLE'])
            print(srno, '. ', i['TITLE'])
            srno += 1

    courseInd = int(input())-1
    found = 0
    searcher = delCourse[courseInd]

    for j in selectedCourses[::-1]:
        if searcher['TITLE'] == j['TITLE']:
            found += 1
            selectedCourses.remove(j)
            if j['SLOT'] in selectedSlots:
                selectedSlots.remove(j['SLOT'])

    if found == 0:
        print("COURSE NOT SELECTED\n")


def dequeue(f, r, k, srno):

    print(srno)
    for keys, values in k.items():
        if keys == 'FACULTY':
            print('\t', keys, ' ' * (10 - len(keys)), ' :    ', values,'\n')
            f = -1
            r = -1
            break
        else:
            print('\t', keys, ' ' * (10 - len(keys)), ' :    ', values)
            f += 1


def enqueue(j, srno):
    f = 0
    r = 0
    for i in j:
        for keys, values in i.items():
            if keys == 'FACULTY':
                d[keys] = values
                srno += 1
                dequeue(f, r, d, srno)
            else:
                d[keys] = values
                r = r + 1


def mergeSort(allCourses):
    if len(allCourses) > 1:
        mid = len(allCourses)//2
        lefthalf = allCourses[:mid]
        righthalf = allCourses[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                allCourses[k] = lefthalf[i]
                i = i+1
            else:
                allCourses[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            allCourses[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            allCourses[k] = righthalf[j]
            j = j+1
            k = k+1


def matchSlot(selectedSlots, checkSlot):
    if checkSlot in selectedSlots:
        return ([False, 'Slot Matching'])

    for i in selectedSlots:
        if checkSlot in i or i in checkSlot and len(selectedSlots) != 0:
            return([False, 'Slot Clashing'])

    coinslots = [["A1", "L1"], ["F1", "L2"], ["D1", "L3"], ["TB1", "L4"], ["TG1", "L5"], ["A2", "L31"],
             ["F2", "L32"], ["D2", "L33"], ["TB2", "L34"], ["TG2", "L35"], ["B1", "L7"], ["G1", "L8"],
             ["E1", "L9"], ["TC1", "L10"], ["TAA1", "L11"], ["B2", "L37"], ["G2", "L38"], ["E2", "L39"],
             ["TC2", "L40"], ["TAA2", "L41"], ["C1", "L13"], ["A1", "L14"], ["F1", "L15"], ["V1", "L16"],
             ["C2", "L43"], ["A2", "L44"], ["F2", "L45"], ["TD2", "L46"], ["TBB2", "L47"], ["D1", "L19"],
             ["B1", "L20"], ["G1", "L21"], ["TE1", "L22"], ["TCC1", "L23"], ["D2", "L49"], ["B2", "L50"],
             ["TE2", "L52"], ["TCC2", "L53"], ["E1", "L25"], ["C1", "L26"], ["TA1", "L27"], ["TF1", "L28"],
             ["TD1", "L29"], ["E2", "L55"], ["C2", "L56"], ["TA2", "L57"], ["TF2", "L58"], ["TDD2", "L59"]]

    for i in coinslots:
        for j in checkSlot.split('+'):
            if j == i[0] and i[1] in '+'.join(selectedSlots).split('+') or j == i[1] and i[0] in '+'.join(selectedSlots).split('+'):
                return([False, 'Slot clashing with some other component'])


    return([True, 'All Good'])


def creditChecker(selectedCourses):
    creditSum = 0
    for i in selectedCourses:
        creditSum += int(i['CREDITS'])
    if creditSum >= 27:
        print('Total Credits: ', creditSum)
        print('Maximum credit limit reached')
        return False

    elif creditSum >= 16:
        print('Total Credits: ', creditSum)
        print('Enter 1 to continue and -1 to stop: ')
        choice = int(input())

        if choice == 1:
            return True
        else:
            return False
    else:
        print('Total Credits: ', creditSum)
        return True


# def coursePrinter(block, srno):
#     print('\n',srno)
#     for i in block.keys():
#         print('\t', i, ' '*(10-len(i)), ' :    ', block[i])
#         srno += 1


def searchIndexer(arr, search):
    results = []
    if search.isdigit():
        return( int(search)-1 )

    else:
        srno =1
        for i in arr:
            if search.lower() in i.lower():
                results.append(i)
                print(srno , '. ', i)
                srno += 1

        if len(results) == 0:
            return(False)
        if len(results) == 1:
            return(int(arr.index(results[0])))

        print('Choose among the following: ')
        chosenResultIndex = int(input())-1

        return(arr.index(results[chosenResultIndex]))


def creator():
    k = 1
    rawdata = demjson.decode(open(r'singleline.json').read().strip('\'')[3:])

    allCourses = []
    for i in rawdata:
        allCourses.append(i['TITLE'])
    allCourses = list(set(allCourses))

    mergeSort(allCourses)

    selectedCourses = []
    selectedSlots = []
    initCreditChecker = True

    for i in range(len(allCourses)):
        print(i + 1, '. ', allCourses[i])

    r=0
    while initCreditChecker:

        printAvailableProjectCourses = []
        chosenCoursesTitle = []
        availableLabProjectCourses = []
        chosenCoursesTitleSingles = []
        availableProjectCourses = []

        print("Choose Course Title: ")
        courseChoice = input()
        chosenIndexCourse = searchIndexer(allCourses, courseChoice)

        if chosenIndexCourse == False:
             print('No such search field found')
             continue

        else:
            for i in selectedCourses:
                if allCourses[chosenIndexCourse] in i['TITLE']:
                    print('Course already taken')
                    continue

        srno = 0
        print('Chosen Course: ', allCourses[chosenIndexCourse])
        for i in rawdata:
            if allCourses[chosenIndexCourse] == i['TITLE']:
                if i['TYPE'] == 'LO' or i['TYPE'] == 'TH' or i['TYPE'] == 'ETH' or i['TYPE'] == 'SS':
                    chosenCoursesTitleSingles.append(i)
                chosenCoursesTitle.append(i)

        enqueue(chosenCoursesTitleSingles, srno)

            #if ------
        print('Choose Course: ')
        chosenIndex = int(input())-1

        if matchSlot(selectedSlots, chosenCoursesTitleSingles[chosenIndex]['SLOT'])[0]:
            selectedCourses.append(chosenCoursesTitleSingles[chosenIndex])
            selectedSlots.append(chosenCoursesTitleSingles[chosenIndex]['SLOT'])

            if chosenCoursesTitleSingles[chosenIndex]['TYPE'] == 'ETH':
                srno = 0
                for i in chosenCoursesTitle:
                    if chosenCoursesTitleSingles[chosenIndex]['FACULTY'] == i['FACULTY'] and i['TYPE'] == 'ELA' and i['CODE'] == chosenCoursesTitleSingles[chosenIndex]['CODE']:
                        availableLabProjectCourses.append(i)

                    if chosenCoursesTitleSingles[chosenIndex]['FACULTY'] == i['FACULTY'] and i['TYPE'] == 'EPJ' and i['CODE'] == chosenCoursesTitleSingles[chosenIndex]['CODE']:
                        availableProjectCourses.append(i)

                enqueue(availableLabProjectCourses, srno)
                #else----
                if len(availableLabProjectCourses) > 0:
                    print('Choose Lab slot: ')
                    chosenIndexLab = int(input())-1

                    if matchSlot(selectedSlots, availableLabProjectCourses[chosenIndexLab]['SLOT'])[0]:
                        selectedCourses.append(availableLabProjectCourses[chosenIndexLab])
                        selectedSlots.append(availableLabProjectCourses[chosenIndexLab]['SLOT'])
                    else:
                        print(matchSlot(selectedSlots, chosenCoursesTitleSingles[chosenIndex]['SLOT'])[1])

                srno = 0
                if len(availableProjectCourses) > 0:
                    for i in availableProjectCourses:
                        if len(availableLabProjectCourses) > 0 and i['SLOT'] == availableLabProjectCourses[chosenIndexLab]['SLOT']:
                            printAvailableProjectCourses.append(i)

                    if len(printAvailableProjectCourses) > 0:
                        enqueue(printAvailableProjectCourses, srno)
                        print('Choose Project Slot: ')
                        chosenIndexProject = int(input()) - 1

                        selectedCourses.append(printAvailableProjectCourses[chosenIndexProject])

                    else:
                        srno = 0
                        enqueue(availableProjectCourses, srno)
                        print('Choose Project Slot: ')
                        chosenIndexProject = int(input()) - 1

                        selectedCourses.append(availableProjectCourses[chosenIndexProject])


        else:
            print(matchSlot(selectedSlots, chosenCoursesTitleSingles[chosenIndex]['SLOT'])[1])

        print(selectedCourses)
        print(selectedSlots)

        print('Do you wish to continue (0) or delete a course (1): ')
        ch = int(input())

        if ch == 1:
            delete(selectedCourses, selectedSlots)

        initCreditChecker = creditChecker(selectedCourses)

    return('+'.join(selectedSlots).split('+'))

if __name__=="__main__":
    print(creator())
