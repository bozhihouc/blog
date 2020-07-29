<div class="citation">
    [#assign i=i+1]
    [#if i lt page.list?size]
    [#include "parent.ftl"]
    [#assign co=page.list[i]]
    [#else]
    [#assign co=comment]
    [/#if]
	<div class="citation-title b">
		<span>[#if co.user??]${co.user.username!?html}[#else]网友[/#if]</span> <em>${page.list?size-i+1}</em>
	</div>
	<p>${co.content?html}</p>
	[#assign i=i-1]
</div>