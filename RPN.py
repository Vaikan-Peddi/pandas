def rpn(num_char,main_stack_string):
##    num_char=input()
##    main_stack_string=input()
    main_stack=main_stack_string.split(" ")
    stack=[]
    for i in range(0,int(num_char)):
        if main_stack[i]=="+":
            a=stack.pop(-1)
            b=stack.pop(-1)
            stack.append(float(a)+float(b))
        elif main_stack[i]=="*":
            a=stack.pop(-1)
            b=stack.pop(-1)
            stack.append(float(a)*float(b))
        elif main_stack[i]=="-":
            a=stack.pop(-1)
            b=stack.pop(-1)
            stack.append(float(b)-float(a))
        elif main_stack[i]=="/":
            a=stack.pop(-1)
            b=stack.pop(-1)
            stack.append(float(b)/float(a))
        else:
            stack.append(main_stack[i])
    return (int(stack[0]))


