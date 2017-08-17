package rpc;

/**
 * 服务提供者：<br>
 * 		运行在服务端，负责提供接口定义，和服务实现类
 * @author kaiLee
 *
 */
public interface EchoService {
	String echo( String ping);
}
