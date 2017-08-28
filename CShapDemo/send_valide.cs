

using System; 
using System.Collections.Generic; 
using System.Linq; 
using System.Web; 
using System.Web.UI; 
using System.Web.UI.WebControls; 
using System.Data.SqlClient; 

///发送邮箱验证
namespace CSDN
{ 
public partial class cheng : System.Web.UI.Page 
{ 
protected void Page_Load(object sender, EventArgs e) 
{ 
//取出参数id 
int id = Convert.ToInt32(Request["id"]); 
string activeCode = Request["activecode"].ToString(); 
//2判断id为id的记录是否存在 
//连接数据库 
string conStr = "data source=LOVE-PC\\SQLEXPRESSPC;initial catalog=Blogs;user id=sa;password=admin"; 
int number; 
using (SqlConnection con = new SqlConnection(conStr)) 
{ 
string sql = "select count(*) from T_User where Id=@id"; 
using (SqlCommand cmd = new SqlCommand(sql, con)) 
{ 
con.Open(); 
cmd.Parameters.AddWithValue("@id", id); 
number = Convert.ToInt32(cmd.ExecuteScalar()); 
} 
} 
if (number > 0) 
{ 
//如果该用户存在取出ActiveCode字段进行比较。如果一样，把Active字段修改为true 
//连接数据库 
string AC; 
using (SqlConnection con = new SqlConnection(conStr)) 
{ 
string sql = "select ActiveCode from T_User where Id=@id"; 
using (SqlCommand cmd = new SqlCommand(sql, con)) 
{ 
con.Open(); 
cmd.Parameters.AddWithValue("@id", id); 
AC = cmd.ExecuteScalar().ToString(); ; 
} 
} 
if (activeCode == AC) 
{ 
Response.Write("激活成功!<a href='denglu.aspx'>返回登录</a>"); 
using (SqlConnection con = new SqlConnection(conStr)) 
{ 
string sql = "update T_User set Active=1 where Id=@id"; 
using (SqlCommand cmd = new SqlCommand(sql, con)) 
{ 
con.Open(); 
cmd.Parameters.AddWithValue("@id", id); 
number = Convert.ToInt32(cmd.ExecuteScalar()); 
} 
} 
} 
else
{ 
Response.Write("用户已存在，但是激活码错误！"); 
} 
} 
else 
{ 
Response.Write("用户不存在，还没注册成功！"); 
} 
} 
} 
} 