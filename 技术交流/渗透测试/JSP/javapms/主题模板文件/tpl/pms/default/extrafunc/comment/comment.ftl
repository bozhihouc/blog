[#assign i=i+1]
[#if i lt page.content?size]
[#if page.content[i].checked]
<div class="citation">
    [#include "comment.ftl"]
    [#assign co=page.content[i]]
	<div class="citation-title b">
		<span>[#if co.user??]${co.user.username!?html}[#else]网友[/#if]</span> <em>#${page.content?size-i+1}</em>
	</div>
	<p>${co.content?html}</p>
</div>
[#else]
[#include "comment.ftl"]
[/#if]
[#else]
<div class="citation">
	<div class="citation-title b">
		<span>[#if comment.user??]${comment.user.username!?html}[#else]网友[/#if]</span> <em>#${1}</em>
	</div>
	<p>${comment.content?html}</p>
</div>
[/#if]
[#assign i=i-1]