import{_ as R}from"./bot-avatar-CBCRm2Zm.js";import{u as v}from"./useBots-CPs4qo_0.js";import{r as g,u as h}from"./utils-CnoIDJDJ.js";import{r as q}from"./router-DJXd_7gP.js";import{g as K}from"./index-QFS3TB7J.js";import{d as N,a1 as V,r as k,aT as j,am as A,a2 as d,a3 as u,M as n,e as B,a4 as r,a8 as y,F as D,a5 as M,L as O,af as C,a6 as P,aa as Q,ab as G,ac as H}from"./index-De9HRGdb.js";import{S as J}from"./index-CaRYvM7w.js";const U=c=>(Q("data-v-e6346cfb"),c=c(),G(),c),W={class:"bot-edit"},X={key:0,class:"loading"},Y={key:1},Z={class:"header"},tt=U(()=>r("img",{src:R,alt:"avatar"},null,-1)),et={class:"name"},st={class:"tabs"},at=["onClick"],ot=N({__name:"BotEdit",setup(c){const{getCurrentRoute:L,changePage:_}=q(),{tabIndex:m,curBot:i}=V(v()),{setTabIndex:w,setCurBot:I,setKnowledgeList:S}=v(),p=K().bots,x=[{name:p.edit,value:0},{name:p.publish,value:1}],l=k(null),f=k(!0),E=j(O,{style:{fontSize:"48px"},spin:!0}),T=async t=>{try{let s=[...(await g(await h.kbList())).filter(e=>!/.*_FAQ$/.test(e.kb_name))];console.log("kbs",s,t),t&&t.length?s=s.map(e=>(t.some(o=>o===e.kb_id)?e.state=1:e.state=0,e)):s=s.map(e=>(e.state=0,e)),console.log("kbs2",s),S(s)}catch(a){C.error(a.msg||"获取知识库列表失败")}},$=async t=>{try{const a=await g(await h.queryBotInfo({bot_id:t}));I(a[0]),T(a[0].kb_ids),f.value=!1}catch(a){C.error(a.msg||"获取Bot信息失败")}};z();function z(){const t=L();console.log("zj-route",t),l.value=t.value.params.botId,$(l.value)}function F(t){t===1&&(!i.value.kb_ids||!i.value.kb_ids.length)||m.value!==t&&(w(t),_(t===0?`/bots/${l.value}/edit`:`/bots/${l.value}/publish`))}return(t,a)=>{var e;const b=J,s=A("router-view");return d(),u("div",W,[n(f)?(d(),u("div",X,[B(b,{indicator:n(E)},null,8,["indicator"])])):(d(),u("div",Y,[r("div",Z,[tt,r("div",et,y((e=n(i))==null?void 0:e.bot_name),1),r("div",st,[(d(),u(D,null,M(x,o=>r("div",{class:P(["tab-item",n(m)===o.value?"tab-active":"",(!n(i).kb_ids||!n(i).kb_ids.length)&&o.value===1?"tab-disable":""]),key:o.name,onClick:nt=>F(o.value)},y(o.name),11,at)),64))])]),B(s)]))])}}}),mt=H(ot,[["__scopeId","data-v-e6346cfb"]]);export{mt as default};
