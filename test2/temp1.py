list_of_supported_cities = ["合肥", "芜湖", "马鞍山", "安庆", "阜阳", "北京", "重庆", "福州", "厦门", "泉州", "龙岩",
                            "漳州", "广州", "深圳", "珠海", "佛山", "江门", "湛江", "肇庆", "惠州", "东莞", "中山",
                            "清远", "南宁", "柳州", "桂林", "北海", "防城港", "贵阳", "黔南", "遵义",
                            "黔西南布依族苗族自治州", "兰州", "天水", "石家庄", "唐山", "邯郸", "邢台", "保定", "廊坊",
                            "承德", "秦皇岛", "张家口", "哈尔滨", "郑州", "开封", "洛阳", "平顶山", "安阳", "新乡",
                            "焦作", "濮阳", "许昌", "漯河", "南阳", "商丘", "周口", "驻马店", "济源", "武汉", "黄石",
                            "宜昌", "襄阳", "鄂州", "孝感", "荆州", "仙桃", "黄冈", "咸宁", "长沙", "株洲", "湘潭",
                            "衡阳", "岳阳", "常德", "永州", "湘西土家族苗族自治州", "海口", "三亚", "五指山", "儋州",
                            "万宁", "澄迈", "乐东", "陵水", "长春", "吉林", "南京", "无锡", "徐州", "常州", "苏州",
                            "常熟", "张家港", "昆山", "南通", "连云港", "淮安", "盐城", "扬州", "镇江", "丹阳", "海门",
                            "句容", "启东", "如皋", "江阴", "海安", "南昌", "景德镇", "萍乡", "九江", "赣州", "吉安",
                            "宜春", "抚州", "上饶", "沈阳", "大连", "抚顺", "丹东", "呼和浩特", "包头", "赤峰", "通辽",
                            "巴彦淖尔", "银川", "太原", "大同", "运城", "晋中", "上海", "济南", "青岛", "淄博", "烟台",
                            "潍坊", "济宁", "泰安", "威海", "临沂", "德州", "菏泽", "成都", "攀枝花", "泸州", "德阳",
                            "绵阳", "遂宁", "内江", "南充", "眉山", "宜宾", "达州", "雅安", "巴中", "资阳",
                            "凉山彝族自治州", "乐山", "广元", "西安", "宝鸡", "咸阳", "渭南", "汉中", "天津",
                            "乌鲁木齐", "昆明", "丽江", "西双版纳傣族自治州", "大理", "杭州", "宁波", "温州", "嘉兴",
                            "湖州", "绍兴", "金华", "义乌", "衢州", "舟山", "台州"]

list_of_all_cities_with_prices = [("石嘴山", 10.48), ("中卫", 11.05), ("吴忠", 11.24), ("朔州", 11.87), ("抚州", 12.08),
                                  ("宿州", 12.18), ("阜阳", 12.27), ("菏泽", 12.31), ("吕梁", 12.33), ("钦州", 12.4),
                                  ("滨州", 12.44), ("泰安", 12.51), ("资阳", 12.56), ("东营", 12.58), ("德州", 12.59),
                                  ("周口", 12.74), ("遂宁", 12.78), ("巴中", 12.8), ("广安", 12.8), ("乌兰察布", 12.83),
                                  ("张掖", 12.88), ("防城港", 12.9), ("晋中", 12.9), ("巴彦淖尔", 12.98),
                                  ("文山", 13.03), ("黔南", 13.1), ("衡水", 13.18), ("鹤岗", 13.29), ("漯河", 13.31),
                                  ("昭通", 13.38), ("潍坊", 13.45), ("博州", 13.56), ("曲靖", 13.6), ("汉中", 13.61),
                                  ("淮北", 13.64), ("毕节", 13.64), ("阳泉", 13.66), ("楚雄", 13.67), ("淮南", 13.73),
                                  ("济宁", 13.79), ("驻马店", 13.81), ("双鸭山", 13.82), ("黔西南", 13.86),
                                  ("忻州", 13.88), ("铁岭", 13.91), ("邢台", 13.95), ("运城", 13.96), ("白山", 13.98),
                                  ("商丘", 14.14), ("娄底", 14.14), ("许昌", 14.2), ("开封", 14.2), ("安阳", 14.25),
                                  ("商洛", 14.27), ("日照", 14.28), ("安顺", 14.3), ("临沂", 14.48), ("六安", 14.51),
                                  ("营口", 14.57), ("南阳", 14.6), ("海东", 14.64), ("牡丹江", 14.69), ("濮阳", 14.71),
                                  ("聊城", 14.73), ("宝鸡", 14.73), ("昌吉", 14.74), ("怀化", 14.75), ("永州", 14.82),
                                  ("湘潭", 14.83), ("哈密", 14.85), ("北海", 14.89), ("河池", 14.9), ("平顶山", 14.92),
                                  ("安庆", 14.96), ("蚌埠", 15.03), ("鹤壁", 15.08), ("固原", 15.1), ("鄂州", 15.1),
                                  ("枣庄", 15.11), ("七台河", 15.17), ("亳州", 15.18), ("新乡", 15.2),
                                  ("三门峡", 15.21), ("随州", 15.35), ("定西", 15.39), ("雅安", 15.39), ("南充", 15.4),
                                  ("咸宁", 15.41), ("百色", 15.48), ("保山", 15.5), ("乌海", 15.52), ("武威", 15.53),
                                  ("孝感", 15.57), ("邵阳", 15.58), ("来宾", 15.6), ("宿迁", 15.61), ("晋城", 15.63),
                                  ("临汾", 15.64), ("新余", 15.67), ("渭南", 15.67), ("大同", 15.69), ("长治", 15.73),
                                  ("贺州", 15.76), ("信阳", 15.89), ("盘锦", 15.92), ("张家口", 15.94), ("银川", 15.98),
                                  ("内江", 15.99), ("黄冈", 16), ("玉林", 16.01), ("自贡", 16.06), ("云浮", 16.09),
                                  ("平凉", 16.14), ("酒泉", 16.2), ("梅州", 16.21), ("河源", 16.22), ("黄石", 16.26),
                                  ("齐齐哈尔", 16.28), ("沧州", 16.29), ("眉山", 16.3), ("清远", 16.31),
                                  ("淮安", 16.35), ("葫芦岛", 16.36), ("黔东南", 16.4), ("松原", 16.4), ("四平", 16.43),
                                  ("安康", 16.43), ("广元", 16.44), ("荆州", 16.45), ("玉溪", 16.45), ("陇南", 16.51),
                                  ("池州", 16.51), ("荆门", 16.52), ("红河", 16.52), ("乐山", 16.58), ("黄山", 16.59),
                                  ("达州", 16.62), ("吉安", 16.63), ("德阳", 16.7), ("泸州", 16.71), ("宣城", 16.76),
                                  ("鹰潭", 16.78), ("白银", 16.89), ("十堰", 16.89), ("绥化", 16.92), ("恩施", 16.92),
                                  ("崇左", 16.93), ("白城", 16.97), ("绵阳", 17), ("黑河", 17.03), ("保定", 17.11),
                                  ("贵港", 17.11), ("阜新", 17.12), ("徐州", 17.34), ("承德", 17.38), ("六盘水", 17.39),
                                  ("马鞍山", 17.4), ("唐山", 17.42), ("铜仁", 17.42), ("锡林郭勒", 17.46),
                                  ("滁州", 17.46), ("焦作", 17.47), ("湘西", 17.47), ("鸡西", 17.55), ("桂林", 17.56),
                                  ("淄博", 17.61), ("包头", 17.65), ("嘉峪关", 17.68), ("九江", 17.68), ("镇江", 17.68),
                                  ("通化", 17.71), ("朝阳", 17.72), ("株洲", 17.81), ("韶关", 17.85), ("巴州", 17.87),
                                  ("洛阳", 17.91), ("抚顺", 17.94), ("海西", 17.94), ("阳江", 17.95), ("佳木斯", 18.02),
                                  ("铜陵", 18.02), ("常德", 18.08), ("益阳", 18.12), ("呼伦贝尔", 18.12),
                                  ("岳阳", 18.13), ("临夏", 18.23), ("赤峰", 18.33), ("郴州", 18.35), ("普洱", 18.4),
                                  ("梧州", 18.45), ("伊犁", 18.46), ("廊坊", 18.49), ("咸阳", 18.5), ("德宏", 18.6),
                                  ("秦皇岛", 18.61), ("锦州", 18.72), ("邯郸", 18.74), ("遵义", 18.8), ("临沧", 18.81),
                                  ("威海", 18.96), ("儋州", 18.97), ("丹东", 18.99), ("辽源", 19.05), ("辽阳", 19.07),
                                  ("景德镇", 19.09), ("上饶", 19.1), ("鞍山", 19.18), ("宜春", 19.24), ("萍乡", 19.27),
                                  ("喀什", 19.31), ("襄阳", 19.35), ("连云港", 19.49), ("衡阳", 19.53), ("泰州", 19.71),
                                  ("通辽", 19.78), ("攀枝花", 19.78), ("芜湖", 19.85), ("烟台", 19.92), ("吉林", 19.99),
                                  ("南平", 20.17), ("汕尾", 20.23), ("呼和浩特", 20.32), ("天水", 20.35),
                                  ("金昌", 20.39), ("大庆", 20.41), ("延边", 20.52), ("茂名", 20.58), ("太原", 20.77),
                                  ("丽江", 20.79), ("肇庆", 20.82), ("盐城", 20.9), ("兴安", 21.09), ("阿克苏", 21.1),
                                  ("柳州", 21.21), ("宜昌", 21.24), ("南通", 21.34), ("赣州", 21.37), ("林芝", 21.39),
                                  ("庆阳", 21.4), ("延安", 21.43), ("张家界", 21.49), ("本溪", 21.52), ("中山", 21.57),
                                  ("惠州", 21.6), ("揭阳", 21.66), ("潮州", 21.84), ("凉山", 22.18), ("石家庄", 22.65),
                                  ("衢州", 22.75), ("龙岩", 22.78), ("宜宾", 22.85), ("江门", 23.4), ("南昌", 23.42),
                                  ("郑州", 23.46), ("鄂尔多斯", 23.53), ("贵阳", 23.6), ("扬州", 23.9), ("湛江", 24.05),
                                  ("常州", 24.37), ("泉州", 24.42), ("南宁", 24.44), ("长春", 24.61), ("漳州", 24.63),
                                  ("嘉兴", 24.69), ("绍兴", 24.8), ("乌鲁木齐", 24.8), ("昆明", 24.81), ("莆田", 24.84),
                                  ("三明", 24.97), ("和田", 25.32), ("榆林", 25.35), ("哈尔滨", 25.41), ("沈阳", 25.66),
                                  ("湖州", 25.67), ("克拉玛依", 25.97), ("佛山", 26.18), ("重庆", 26.59),
                                  ("大理", 26.69), ("兰州", 27.02), ("无锡", 27.31), ("东莞", 27.38), ("宁德", 27.62),
                                  ("西宁", 27.8), ("济南", 27.98), ("青岛", 28.67), ("丽水", 28.7), ("合肥", 29.08),
                                  ("拉萨", 29.38), ("金华", 29.61), ("长沙", 29.78), ("温州", 29.85), ("台州", 29.97),
                                  ("西双版纳", 30.14), ("西安", 31.2), ("舟山", 31.4), ("海口", 31.87), ("大连", 32.04),
                                  ("汕头", 32.7), ("宁波", 34.03), ("苏州", 35.54), ("珠海", 37.39), ("福州", 38.26),
                                  ("天津", 41.73), ("成都", 45.42), ("厦门", 48.81), ("三亚", 51.39), ("武汉", 53.71),
                                  ("南京", 61.08), ("广州", 61.98), ("杭州", 71.85), ("深圳", 105.23), ("上海", 113.63),
                                  ("北京", 124.77)]

list_of_supported_cities_with_prices = []

for city_tuple in list_of_all_cities_with_prices:
    if city_tuple[0] in list_of_supported_cities:
        list_of_supported_cities_with_prices.append(city_tuple)

list_of_supported_cities_with_prices.sort(key=lambda city_tuple_item: city_tuple_item[1])

print(list_of_supported_cities_with_prices)