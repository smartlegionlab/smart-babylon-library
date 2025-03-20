# Smart Babylon Library <sup>v0.1.0</sup>

***

![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smart_babylon_library)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smart_babylon_library)](https://github.com/smartlegionlab/smart_babylon_library/)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smart_babylon_library)](https://github.com/smartlegionlab/smart_babylon_library/blob/master/LICENSE)
[![GitHub Repo stars](https://img.shields.io/github/stars/smartlegionlab/smart_babylon_library?style=social)](https://github.com/smartlegionlab/smart_babylon_library/)
[![GitHub watchers](https://img.shields.io/github/watchers/smartlegionlab/smart_babylon_library?style=social)](https://github.com/smartlegionlab/smart_babylon_library/)
[![GitHub forks](https://img.shields.io/github/forks/smartlegionlab/smart_babylon_library?style=social)](https://github.com/smartlegionlab/smart_babylon_library/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smart_babylon_library?label=pypi%20downloads)](https://pypi.org/project/smart_babylon_library/)
[![PyPI](https://img.shields.io/pypi/v/smart_babylon_library)](https://pypi.org/project/smart_babylon_library)
[![PyPI - Format](https://img.shields.io/pypi/format/smart_babylon_library)](https://pypi.org/project/smart_babylon_library)

***

Author and developer: ___A.A. Suvorov___

***

## Description:

# __smart_babylon_library__

BabylonLibrary is a Python library inspired by the concept of the Babylonian Library 
that allows generating unique coordinates for texts. 
These coordinates provide constant access to texts that are not physically stored anywhere, 
but can only be retrieved by previously generated addresses. 
This allows users to find and retrieve information by specified parameters.

## Main features:

- **Generate Unique Coordinates**: Create unique coordinates in the form of addresses for texts that can be used for subsequent search.
- **Search by Address**: Extract text using a previously generated address.
- **Custom Character Set**: Use your own character set to encode and decode texts.
- **Convert between number systems**: Support for different number systems for encoding library addresses.
- **Generate Random Coordinates**: Generate random coordinates and extract texts that may be located at these addresses.

## Installation:

To use __smart_babylon_library__, simply clone the repository:

```bash
git clone https://github.com/smartlegionlab/smart_babylon_library.git
cd smart_babylon_library
```

## Example of use:

```python
from smart_babylon_library import BabylonLibrary

library = BabylonLibrary()

# Getting a unique address for your text
unique_address = library.search_by_content("your text")
print(f"Unique address: {unique_address}")

# Getting text from a previously received unique address
address_result = library.search_by_address(unique_address)
print(f"Result: {address_result}")

```

## Configuration

You can customize the library's behavior by changing parameters in the `BabylonLibrary` constructor:

- `charset`: The character set used to encode content.
- `max_page_content_length`: The maximum length of content on a page.
- `max_walls`: The maximum number of walls in a library.
- `max_shelves`: The maximum number of shelves in a library.
- `max_volumes`: The maximum number of volumes in a library.
- `max_pages`: The maximum number of pages in a volume.
- `hexagon_base`: The base used to encode library addresses.

## Use:

```python
from smart_babylon_library import BabylonLibrary
from smart_babylon_library.tools import timeit


@timeit
def main():
    library = BabylonLibrary()

    text_to_search = 'test'

    full_address = library.search_by_content(text_to_search)

    print(f"Address for text '{text_to_search}': {full_address}")

    content_result = library.search_by_address(full_address)

    print(f"Contents at address '{full_address}': {content_result}")


if __name__ == '__main__':
    main()


```

Output:

```
Address for text 'test': 1m1i0nftdvvzcca2ut6i3belca42zi16m6zzllgm1n7wpgcv0jjo8fadlkfzk6ysyxsnkcoe3egb1oa64x22rwwbvu19focifcpweezvlp2ab0jso01wyw4xfgwypenmuer1oabaes92p92ypy12wl6l2cf7jc7i4u9mtcbc6zyst48ansgky2z9mqgfp97bwmq7aouisub0d3isv8bs68a6qxpx07h6ayzk3u6d87c8osfmtbiqo4tcdrwt8s7bne2eqep46jbnc2f96uwsqnu9v15tqsrhxrinjh8fd9nz3bd64ubc3y0fw8snnvyswp7fb90bihi93wybgvdk8loatbipqkz5dsybv2ekmzig0ibnyhr5ej5dw2k6kgrh5qncpw63g1dbgn4nuadk8undu4fz3aivh6nf6gorhxyyf2wm6lql5hb2esfmz0fji56mv13o5unnlpjx97cgk4nv82oyc3iarrnslis0agtq8ehm44zx0pxbuzs0i4tfk78q9tis73a375lhgyjko3108117x3odzuke0oit2pwp6toyel3jclututmnbcsbg7fdeybd8uimygw0lfypov6zp503rah0lxibvh5ujpxqxq1sfpelpwwjj275bet9jzlxgfihfeeo6b175224owo9z9kq2hxxm8vnguckzzzmc2jfbpchk78k8da7nj66i6j6c0xsxbjbghct6afgk9uo48tlrbflajg6apg0mjj89fzvhutqm6urtnt2zecr5zhlxdvjudgmue5u40vj3bwrxbre557kvjwdmd26cn0e4gy2ivsyd6b7vfmbbm2uiucxnvgszgi3lf97lffsbussmyd9aqlsyfhjww1poqgandwpmgh56jm67y37s4ryifkn82bmj3nj0whz9bp91dana0c7a6lf2bal2wwre4mvwy3p3f5mlgitzprf8uve4ybqymj6h2zs9hdorvz1pc7tfzm7ejx2uk6jojkq4f4m4iy26nn5toup53yedc7dybazaxirb459tuza69n88zcj127v3hond7qky0uon2689tbjrc3c4rz9jtjffoeoglaw3axmjz9tk40urk2fbwvwpxiw5gdn9v5m9yjz878orj8glxmd0eqklcjnizr7r55rgqwm6v1h1q1r4309pvds0of6sybfinmr6ygj328rpqj7jscglhpmtvxzbsmbvo6p8d1oeiltll8dhym5nqlskj4e00g973ny5gsx829bfte5qwh8rq1mgwlx01p2dcy5lqwhmk2oe5ri53vmbn7wo756mss8uc9y6uavl7ny1trrivgujkdueyl026y8llq10jsgz74nw6s10jrv90ov1fx72pnqdh7h05ikcysb79e99p50k5w3urliiyj60i4uimscb7wsht7twqk01re4560io73hvfboa7s0wahkhqjh053rn6772c648vezof37bihretwiauxblr0g937imj1ibly3s81vamhnsfbgw420x4tutfnwl7pm30qeugspiytln8iuwf5othforp8kbmkqxiemzs9n9xo6o94f65brfty0vk01esxdwz3hfl2krl2y2kcho6ys38opy47vryvdm0uex07nfbknax4v6dk2rs4o0cc1pluf4p6dcmjcbuc99g9rse00oxaznztz7fggfptif6owmbu8kvgyl0k2wi9dozd5fi6pnau9ykai80i0edk7pbt8czzyls0zmc08x8bsqt58iequrc40amydw78zq25gkh7wl4e65a5ual0gmstfn80gfb4vaqo1axysmoykn52vrivalzdynil2sexapxgfkbnh2jdmmxwf3ozgsw8g59n4e79u7p4idk85zvvwbuw3qbcm1xf19zi9sif3gruufe86bpcaxkgh9nngs6nqhqpbr7vxnkgn0y2vi7jlrhzb3zdjuqdcd1ya7ednpz29mazigooiau446bldvryp40wp37b5p9ittkyaw3lqfmlrpstwdcarbjqcxamp081pjeyc5tf1qg4v9h8dhzk71s80x8vnc73ghucq33ofafimwy7sso90gjmo4iorjo0a2o77epni1830zajm9vfhsnf0cxzkdh3fc4zj7xltc1ih3c5674duwfh6kbti4h542mp7tmwihgqj9v68whzpxbkri3rjd56edywskqdn4rs9jccis4ul97ddvhh2tjtj9xwt8ztix7ujz7w3agx5umxtf1r7qytiycmabllxeqgyi5scwef2zwdfoemmixy00sd9i4635fstbnoy87p7sxkovj1gkc72syehrpkrwntys52p9u3kiglduz79lb55bq9s79urwul73j5ciwmnmd142djg3ie5uszrt4a45b1pqh1p05e3uoc01037m06cc4df01hltjiiu8a5ka3qr69m87wykjcozfdo78u4zi18ndx5we1q4zknpp2g94d85vejhvr8yv0p7jyxckntivsvnjqlbjm9i0cbpvl7ynp5emjoo53vn61jrh6d7o4gtu3b1zuq83lkkkzevb8bd9dgfa5usv8y8g96axetrvmxf84wkno425ij8v1809s5lac32rp41ciz3ekrf7giv8l11jwhdy2y8sw52vysky7ihz72bxhcrlzvcpvln7l7zh94wvovef0jk4p3go73elj7kth0wqw2fp551fry353rsapll8yjppw62izqkgzlgw7phtfbsrtybec0f7uyss4i0gfazr1940gu2zoiyyu91580hl6p2qw765oq5pd3lvgpoagw91kvi597ymv5anb6smo4rltuwpv7yosssh86rrcxswkz3up1otuoh7n1whd81prr62lc49b8pxs78u4qlqfsgz9f93yrvjakdl0ofj0ibcj5zryi0bq1hzf2in0cfsv0rkixdsfkwsvhdle9yk4veyckl3x2pbp69t5txza77r7a784v0whb3iamnypwh26yi9n:1:01:01:001
Contents at address '1m1i0nftdvvzcca2ut6i3belca42zi16m6zzllgm1n7wpgcv0jjo8fadlkfzk6ysyxsnkcoe3egb1oa64x22rwwbvu19focifcpweezvlp2ab0jso01wyw4xfgwypenmuer1oabaes92p92ypy12wl6l2cf7jc7i4u9mtcbc6zyst48ansgky2z9mqgfp97bwmq7aouisub0d3isv8bs68a6qxpx07h6ayzk3u6d87c8osfmtbiqo4tcdrwt8s7bne2eqep46jbnc2f96uwsqnu9v15tqsrhxrinjh8fd9nz3bd64ubc3y0fw8snnvyswp7fb90bihi93wybgvdk8loatbipqkz5dsybv2ekmzig0ibnyhr5ej5dw2k6kgrh5qncpw63g1dbgn4nuadk8undu4fz3aivh6nf6gorhxyyf2wm6lql5hb2esfmz0fji56mv13o5unnlpjx97cgk4nv82oyc3iarrnslis0agtq8ehm44zx0pxbuzs0i4tfk78q9tis73a375lhgyjko3108117x3odzuke0oit2pwp6toyel3jclututmnbcsbg7fdeybd8uimygw0lfypov6zp503rah0lxibvh5ujpxqxq1sfpelpwwjj275bet9jzlxgfihfeeo6b175224owo9z9kq2hxxm8vnguckzzzmc2jfbpchk78k8da7nj66i6j6c0xsxbjbghct6afgk9uo48tlrbflajg6apg0mjj89fzvhutqm6urtnt2zecr5zhlxdvjudgmue5u40vj3bwrxbre557kvjwdmd26cn0e4gy2ivsyd6b7vfmbbm2uiucxnvgszgi3lf97lffsbussmyd9aqlsyfhjww1poqgandwpmgh56jm67y37s4ryifkn82bmj3nj0whz9bp91dana0c7a6lf2bal2wwre4mvwy3p3f5mlgitzprf8uve4ybqymj6h2zs9hdorvz1pc7tfzm7ejx2uk6jojkq4f4m4iy26nn5toup53yedc7dybazaxirb459tuza69n88zcj127v3hond7qky0uon2689tbjrc3c4rz9jtjffoeoglaw3axmjz9tk40urk2fbwvwpxiw5gdn9v5m9yjz878orj8glxmd0eqklcjnizr7r55rgqwm6v1h1q1r4309pvds0of6sybfinmr6ygj328rpqj7jscglhpmtvxzbsmbvo6p8d1oeiltll8dhym5nqlskj4e00g973ny5gsx829bfte5qwh8rq1mgwlx01p2dcy5lqwhmk2oe5ri53vmbn7wo756mss8uc9y6uavl7ny1trrivgujkdueyl026y8llq10jsgz74nw6s10jrv90ov1fx72pnqdh7h05ikcysb79e99p50k5w3urliiyj60i4uimscb7wsht7twqk01re4560io73hvfboa7s0wahkhqjh053rn6772c648vezof37bihretwiauxblr0g937imj1ibly3s81vamhnsfbgw420x4tutfnwl7pm30qeugspiytln8iuwf5othforp8kbmkqxiemzs9n9xo6o94f65brfty0vk01esxdwz3hfl2krl2y2kcho6ys38opy47vryvdm0uex07nfbknax4v6dk2rs4o0cc1pluf4p6dcmjcbuc99g9rse00oxaznztz7fggfptif6owmbu8kvgyl0k2wi9dozd5fi6pnau9ykai80i0edk7pbt8czzyls0zmc08x8bsqt58iequrc40amydw78zq25gkh7wl4e65a5ual0gmstfn80gfb4vaqo1axysmoykn52vrivalzdynil2sexapxgfkbnh2jdmmxwf3ozgsw8g59n4e79u7p4idk85zvvwbuw3qbcm1xf19zi9sif3gruufe86bpcaxkgh9nngs6nqhqpbr7vxnkgn0y2vi7jlrhzb3zdjuqdcd1ya7ednpz29mazigooiau446bldvryp40wp37b5p9ittkyaw3lqfmlrpstwdcarbjqcxamp081pjeyc5tf1qg4v9h8dhzk71s80x8vnc73ghucq33ofafimwy7sso90gjmo4iorjo0a2o77epni1830zajm9vfhsnf0cxzkdh3fc4zj7xltc1ih3c5674duwfh6kbti4h542mp7tmwihgqj9v68whzpxbkri3rjd56edywskqdn4rs9jccis4ul97ddvhh2tjtj9xwt8ztix7ujz7w3agx5umxtf1r7qytiycmabllxeqgyi5scwef2zwdfoemmixy00sd9i4635fstbnoy87p7sxkovj1gkc72syehrpkrwntys52p9u3kiglduz79lb55bq9s79urwul73j5ciwmnmd142djg3ie5uszrt4a45b1pqh1p05e3uoc01037m06cc4df01hltjiiu8a5ka3qr69m87wykjcozfdo78u4zi18ndx5we1q4zknpp2g94d85vejhvr8yv0p7jyxckntivsvnjqlbjm9i0cbpvl7ynp5emjoo53vn61jrh6d7o4gtu3b1zuq83lkkkzevb8bd9dgfa5usv8y8g96axetrvmxf84wkno425ij8v1809s5lac32rp41ciz3ekrf7giv8l11jwhdy2y8sw52vysky7ihz72bxhcrlzvcpvln7l7zh94wvovef0jk4p3go73elj7kth0wqw2fp551fry353rsapll8yjppw62izqkgzlgw7phtfbsrtybec0f7uyss4i0gfazr1940gu2zoiyyu91580hl6p2qw765oq5pd3lvgpoagw91kvi597ymv5anb6smo4rltuwpv7yosssh86rrcxswkz3up1otuoh7n1whd81prr62lc49b8pxs78u4qlqfsgz9f93yrvjakdl0ofj0ibcj5zryi0bq1hzf2in0cfsv0rkixdsfkwsvhdle9yk4veyckl3x2pbp69t5txza77r7a784v0whb3iamnypwh26yi9n:1:01:01:001': test                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
Execution time: 0.1033 seconds
```


***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2025, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------