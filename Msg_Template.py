from linebot.models import *

def stock_reply_rate():
    content_text = '想知道匯率?'
    text_message = TextSendMessage(
                                 text = content_text ,
                                quick_reply=QuickReply(
                                    items=[
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="💜💜查詢單一幣別匯率", 
                                                    text="幣別種類",
                                                )
                                        ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="💜💜查詢幣別匯率", 
                                                    text="匯率兌換",
                                                )
                                        ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="💜💜關注的匯率", 
                                                    text="我的外幣",
                                                )
                                        ),
                                ]
                            ))
    return text_message

#測試的button
def test_button():
    flex_message = FlexSendMessage(
        alt_text="幣別種類",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/EDIjprs.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "message",
                    "label": "action",
                    "text": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "美金",
                        "text": "USD"
                        },
                        "height": "md",
                        "style": "primary",
                        "margin": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "台幣",
                        "text": "TWD"
                        },
                        "height": "md",
                        "style": "secondary",
                        "margin": "sm"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "印尼盾",
                        "text": "IDR"
                        },
                        "height": "md",
                        "style": "primary",
                        "margin": "sm"
                    }
                    ],
                    "backgroundColor": "#000490"
                }
            }
    )
    return flex_message

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/EDIjprs.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "message",
                    "label": "action",
                    "text": "hello"
                    }
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "美金",
                            "text": "USD"
                            },
                            "height": "md",
                            "style": "primary",
                            "margin": "sm",
                            "color": "#000456"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "日元",
                            "text": "JPY"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#009541"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "港幣",
                            "text": "HKD"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#002645"
                        }
                        ],
                        "borderWidth": "none"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "英鎊",
                            "text": "GBP"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#005874"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "澳幣",
                            "text": "AUD"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#007415"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "加大幣",
                            "text": "CAD"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#008421"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "瑞法郎",
                            "text": "CHF"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "flex": 1,
                            "color": "#000321"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "新幣",
                            "text": "SGD"
                            },
                            "flex": 1,
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#003651"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "南非幣",
                            "text": "ZAR"
                            },
                            "flex": 1,
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#023452"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "瑞典幣",
                            "text": "SEK"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#005613"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "紐元",
                            "text": "NZD"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#A02334"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "泰銖",
                            "text": "THB"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#FFAD60"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "菲比索",
                            "text": "PHP"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#FFEEAD"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "印尼盾",
                            "text": "IDR"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#C75B7A"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "韓元",
                            "text": "KRW"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#F4D9D0"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "馬來幣",
                            "text": "MYR"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#6482AD"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "越南盾",
                            "text": "VND"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#7FA1C3"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "人民幣",
                            "text": "CNY"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#FFDA76"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "台幣",
                            "text": "TWD"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#7C00FE"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "歐元",
                            "text": "EUR"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "secondary",
                            "color": "#F9E400"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "烏索姆",
                            "text": "UZS"
                            },
                            "margin": "sm",
                            "height": "md",
                            "style": "primary",
                            "color": "#FFAF00"
                        }
                        ]
                    }
                    ],
                    "spacing": "sm",
                    "borderWidth": "none"
                },
                "styles": {
                    "footer": {
                    "backgroundColor": "#6EACDA"
                    }
                }
            }
    )
    return flex_message



# 理財頻道
def youtube_channel():
    flex_message = FlexSendMessage(
            alt_text="youtube_channel",
            contents=
            {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/SJPH542.jpg",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "size": "full",
                        "backgroundColor": "#000000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財達人秀",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "最精彩最好懂",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/channel/UCQvsuaih5lE0n_Ne54nNezg"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/dPW0jcC.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#AA0000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CMoney理財寶",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "基本理財知識",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/CMoneySchool"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/zkUZrCj.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#444444"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "我要做富翁",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "平民化&分享形式",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/SyLingHim"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    }
                ]
            }
        )
    return flex_message

def realtime_currency_other(currency):
    content = "想知道更多?"
    text_message = TextSendMessage(
                                text = content ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="即時匯率", 
                                                    text="外幣"+currency,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="加入清單", 
                                                    text="新增外幣"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="走勢圖", 
                                                    text="CT"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text="N外匯"+currency,
                                                )
                                       )
                                ]
                            ))
    return text_message
