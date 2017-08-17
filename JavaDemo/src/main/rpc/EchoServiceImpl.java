package rpc;

/**
 * 服务提供者：<br>
 * 		运行在服务端，负责提供接口定义，和服务实现类
 * @author kaiLee
 * @version 1.0
 * @see EchoService
 *
 */
public class EchoServiceImpl implements EchoService {

	@Override
	public String echo(String ping) {
		// TODO Auto-generated method stub
		return (null != ping)? (ping + "  ---> I am ok . from Mac OX "):(" I am ok. from Mac OX ");
	}
}
