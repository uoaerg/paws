//v2 netfilter hooks example
//For any packet, get the ip header and check the protocol field
//if the protocol number equal to UDP (17), log in var/log/messages
//default action of module to let all packets through
 
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/skbuff.h>
#include <linux/udp.h>
#include <linux/ip.h>
#include <linux/tcp.h>
 
 
unsigned int hook_func(unsigned int hooknum,
					struct sk_buff *skb,
					const struct net_device *in,
					const struct net_device *out,
					int (*okfn)(struct sk_buff *))
{
	static struct nf_hook_ops nfho;   //net filter hook option struct
	struct tcphdr *tcph;          //tcp header struct
	struct iphdr *iph;            //ip header struct

	if (skb)
	{
        iph = ip_hdr(skb);    //grab network header using accessor
       
        if (iph && iph->protocol && (iph->protocol == IPPROTO_TCP)) // check if tcp header available
        {
            tcph = (struct tcphdr *)((__u32 *)iph + iph->ihl);
            
            if (tcph->syn) && (tcph->ack)
            {
            unsigned int dest_ip = (unsigned int)iph->daddr;
            
            printk(KERNEL_INFO "This is a SYN packet with destination address: %u\n ", ntohl(dest_ip) );
            
            }
 
        }
               
       
	}
	 return NF_ACCEPT;	
}
 
int init_module()
{
        nfho.hook = hook_func;
        nfho.hooknum = NF_IP_PRE_ROUTING;
        nfho.pf = PF_INET;
        nfho.priority = NF_IP_PRI_FIRST;
        nf_register_hook(&nfho);
       
        return 0;
}
 
void cleanup_module()
{
        nf_unregister_hook(&nfho);     
}