def getChildText(ctx,i):
        if type(ctx.getChild(i)) == type(ctx):
            t = ctx.getChild(i).getText(transform=False)
        else:
            t = ctx.getChild(i).getText()
        return t

def isAtomic(t):
    if t.getChildCount() == 0:
        # terminal nodes are always atomic
        return True
    if t.getChildCount() > 2:
        if getChildText(t,0) == '<':
            #Exponentiation does not distribute across pairs
            return True 
        elif getChildText(t,1) == '(':
            #Exponentiation does not distribute across functions
            return True 
    for c in range(t.getChildCount()):
        if getChildText(t,c) == "^":
            #There is a direct child using exponentiation
            return False
        elif not isAtomic(t.getChild(c)):
            #Or a child of a child using exponentiation 
            return False
    return True

def isConstant(t):
    #True if all varIdentifier children are constant.
    #varIdentifier's are constant if start with $~ or ''
    if t.getChildCount() == 0:
        return True
    if t.varIdentifier() is not None:
        v = t.varIdentifier().getText()
        if v[0] not in ["'","$","~"]:
            return False
    else:
        for t in t.getChildren():
            if not isConstant(t):
                return False
    return True

def getVar(t):
    o = "" 
    for c in t:
        if not (c.isalnum() or c == '_'):
            #The only other possible values are '()<>$ so 
            #no collisions possible?
            o += 's'
        else:
            o += c
    return o

def makeConstantElement(t):
    return "element('G',grpid,"+t.getText(transform=False)+')'

def makeVarElement(t):
    return "element('G',"+getVar("adv"+t.getText(transform=False))+","+getVar(t.getText(transform=False))+')'

def transformTerm(ctx):
    if ctx.getChildCount() == 3:
        t = getChildText(ctx,1)
        if t == '^':
            if isConstant(ctx):
                return makeConstantElement(ctx)
            else:
                base = ctx.getChild(0)
                if isAtomic(base):
                    return makeVarElement(base) + getChildText(ctx,1) + getChildText(ctx,2) 
    return ctx.getText(transform=False)