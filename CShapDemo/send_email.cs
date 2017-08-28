
    using System; 
    using System.Collections.Generic; 
    using System.Linq; 
    using System.Web; 
    using System.Web.UI; 
    using System.Web.UI.WebControls; 
    using System.Text; 
    using System.Net.Mail; 
    using System.Net; 
    using System.Data.SqlClient; 

    ///发送邮箱验证码
    namespace CSDN 
    { 
    public partial class Registe : System.Web.UI.Page 
    { 
    protected void Page_Load(object sender, EventArgs e) 
    { 
    } 
    protected void CheckBox1_CheckedChanged(object sender, EventArgs e) 
    { 
    } 
    public void sendMail(string email, string activeCode) 
    { 
    MailMessage mailMsg = new MailMessage(); 
    mailMsg.From = new MailAddress("15031259715@163.com"); 
    mailMsg.To.Add(email); 
    mailMsg.Subject = "请激活注册"; 
    int number = number1(); 
    StringBuilder contentBuilder = new StringBuilder(); 
    contentBuilder.Append("请单击以下链接完成激活"); 
    contentBuilder.Append("<a href='http://localhost:15464/cheng.aspx?activecode=" + activeCode + "&id=" + number + "'>激活</a>"); 
    mailMsg.Body = contentBuilder.ToString();//拼接字符串 
    mailMsg.IsBodyHtml = true; 
    SmtpClient client = new SmtpClient(); 
    //发件方服务器地址 
    client.Host = "smtp.163.com"; 
    client.Port = 25; 
    //mailMsg.IsBodyHtml = true; 
    NetworkCredential credetial = new NetworkCredential(); 
    credetial.UserName = "15031259715"; 
    credetial.Password = "wangjing911214++"; 
    client.Credentials = credetial; 
    client.Send(mailMsg); 
    } 
    public int number1() 
    { 
    CSDN博客.BLL.T_User count = new BLL.T_User(); 
    int a = count.GetRecordCount(""); 
    return a; 
    } 
    protected void ImageButton1_Click(object sender, ImageClickEventArgs e) 
    { 
    CSDN博客.Model.T_User muser = new Model.T_User(); 
    muser.Name = txtName.Text; 
    muser.Password = txtPassword.Text; 
    muser.E_Mail = txtEmail.Text; 
    string activecode=Guid.NewGuid().ToString().Substring(0, 8); 
    muser.ActiveCode = activecode;//生成激活码 
    CSDN博客.BLL.T_User buser = new BLL.T_User(); 
    if (buser.Add(muser) > 0) 
    { 
    sendMail(txtEmail.Text, activecode);//给注册用户发邮件 
    lbinfo.Text = "保存成功"; 
    } 
    else { lbinfo.Text = "保存失败"; } 
    } 
    } 
    } 
