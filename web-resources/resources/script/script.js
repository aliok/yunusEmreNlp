/*
 * Copyright [2012] [Ali Ok - aliok@apache.org]
 *
 *    Licensed under the Apache License, Version 2.0 (the "License");
 *    you may not use this file except in compliance with the License.
 *    You may obtain a copy of the License at
 *
 *        http://www.apache.org/licenses/LICENSE-2.0
 *
 *    Unless required by applicable law or agreed to in writing, software
 *    distributed under the License is distributed on an "AS IS" BASIS,
 *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *    See the License for the specific language governing permissions and
 *    limitations under the License.
 */

function showTip(elem){
    $(elem).tipsy("show");
    $(elem).attr('tip-visible', true);
    $(elem).addClass('word-highlight');
}

function hideTip(elem){
    $(elem).tipsy("hide");
    $(elem).attr('tip-visible', false);
    $(elem).removeClass('word-highlight');
}

function toggleLineTips(element){
    var parent = $(element).parent();
    var visible = parent.attr('tip-visible');

    $.each(parent.children("a.tip"), function(){
        if (visible === "true") {
            hideTip(this);
        } else{
            showTip(this);
        }
    });

    if(visible === "true"){
        parent.attr('tip-visible', false);
    } else{
        parent.attr('tip-visible', true);
    }

    return false;
}

function showAllTips(){
    $.each($("#container a.tip"), function(){
        showTip(this);
    });
    $('p.line').attr('tip-visible', true);
}

function hideAllTips(){
    $.each($("#container a.tip"), function(){
        hideTip(this);
    });
    $('p.line').attr('tip-visible', false);
}

$('#container a.tip').tipsy({gravity:'s', trigger:'manual'});
$('#container a.tip').bind('click', function () {
    var visible = $(this).attr('tip-visible');
    if (visible === "true") {
        hideTip(this);
    } else {
        showTip(this);
    }
    return false;
});


$("a.lineTipToggler").bind("click", function(){
    toggleLineTips(this);
    return false;
});

function setAsLastPage(url, title){
    if(window.localStorage){
        window.localStorage['lastUrl'] = url;
        window.localStorage['lastTitle'] = title;
    }
}

function getLastPageUrl(){
    if(window.localStorage){
        return window.localStorage['lastUrl'];
    }

    return null;
}

function getLastPageTitle(){
    if(window.localStorage){
        return window.localStorage['lastTitle'];
    }

    return null;
}

function setNextPageLink(nextPageUrl){
    if(nextPageUrl && nextPageUrl!==''){
        $('#nextPageLink').attr('href', nextPageUrl);
        $('#nextPageBlock').css('display', 'block');
    }
}