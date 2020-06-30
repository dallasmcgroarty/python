# var obj = {foo: {bar:99}};
# resolve(obj, 'foo') // returns {bar:99}
# resolve(obj, 'foo.bar') // returns 99var 
# obj = {a:1,"helb:lo", c:{d:"foo"}}

# resolve(obj, "c.d") -> "foo"
# resolve(obj, "a") -> 1
# resolve(obj, "b") -> "hello"
# resolve(obj, "c") -> {d: "foo"}
# resolve(obj, "c.d") -> "foo"



def resolve(obj, key):
    arr_keys = key.split('.')
    # # [c,d,b]
    ret_obj = obj
    for i in arr_keys:
        ret_obj = ret_obj[i]
    return ret_obj
    # # 0 = d
    # # d = d[b]
    # if obj.get(key):
    #     return obj[key]
    # else:
    #     resolve(obj[key],key)

o = {'a':1,'b':{'c':1}}

print(resolve(o,'b.c'))