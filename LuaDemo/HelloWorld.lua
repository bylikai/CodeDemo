#!/usr/local/bin/lua

print("Hello World! Lua")

--print("www.baidu.com")

--[[
print("www.google.com")
]]--

html = [[
<html>
<head></head>
<body>
    <a href="http://www.runoob.com/">菜鸟教程</a>
</body>
</html>
]]
print(html)

local tbl1={}
local tbl2={"apple", "pear", "orange", "grape"}
local tbl3 = {}
tbl3["lk"]=36
tbl3[12] = 12*3

for k,v in pairs(tbl3) 
do 
    print(k.." : "..v)
end

local m = 12
m = m + 4

print(m)

hello = "hello" .. " world"
print(hello)


--[ 定义变量 --]
a = 100;
--[ 检查条件 --]
if( a < 20 )
then
   --[ if 条件为 true 时执行该语句块 --]
   print("a 小于 20" )
else
   --[ if 条件为 false 时执行该语句块 --]
   print("a 大于 20" )
end

local hello_reverse = string.reverse(hello)
print( hello_reverse )
print( string.lower(hello_reverse) )
print( string.upper(hello_reverse) )

print( string.find(hello, "world"), 1 )



require("module_test")
print(module.constant)
module.func3()