# Macで作成したZip群からいらないファイルを除去する(Win用)

import glob
import os
import sys
import zipfile
import shutil

FromDir = 'D:/work/sango_new/'  #ここにzipファイル群を入れておく（Macで圧縮したやつ
TmpDir = 'D:/work/sango_tmp'    #こちらが出力フォルダ  


#ループ元
#files = glob.glob("D:/work/sango_new/*")
ffiles = glob.glob(FromDir+"*")

for ffile in ffiles:
    #print(ffile)
    full_name = ffile
    print(full_name)
    dir_name = os.path.dirname(full_name)
    print(dir_name)

    basename = os.path.basename(full_name)
    print(basename)

    basename_without_ext = os.path.splitext(basename)[0]
    print(basename_without_ext)    

    #sys.exit()

    #    print(file[0:18]+file[-6:])
    ##    os.rename(file,file[0:18]+file[-6:])



    #以下ループ内動作


    # Zipファイルを解凍
    #with zipfile.ZipFile('D:/work/sango_new/02.zip') as existing_zip:
    #with zipfile.ZipFile(FromDir+'02.zip') as existing_zip:
    with zipfile.ZipFile(full_name) as existing_zip:
        #print(existing_zip.namelist())
        existing_zip.extractall(TmpDir)
        #existing_zip.extract('*.PNG', 'D:/work/sango_new/tmp')

    print('解凍')


    #__MACOSX/ フォルダがあったら邪魔なので消しておく
    if(os.path.exists(TmpDir+'/__MACOSX')):
        shutil.rmtree(TmpDir+'/__MACOSX/')
        print('__MACOSX削除')
    

    #ファイルリスト再確認
    files = glob.glob(TmpDir+"/*")
    for file in files:
        print(file)

    # ↑最期のfile が ＞ 'D:/work/sango_tmp\µ¿¬σ▒▒σàëΦ╝¥_Σ╕ëσ¢╜σ┐ù_02' こんなののはず
    # ループの外でも見れるかチェック
    #print(file) # OK
    # ↑このほうほうはバグ呼びそう。まあ動いているからいいや。

    # .DS_Store 邪魔なので消しておく
    if(os.path.exists(file+'/.DS_Store')):
        os.remove(file+'/.DS_Store')
        print('.DS_Store削除')
    

    #ディレクトリ名変えておく
    #os.rename(file, TmpDir+"/02")
    os.rename(file, TmpDir+"/"+basename_without_ext)
    print('ディレクトリ名変更>'+basename_without_ext)

    #アーカイブ
    print('アーカイブ作成開始')
    #shutil.make_archive('D:/work/sango_tmp/02', 'zip', root_dir='D:/work/sango_tmp/02')
    #shutil.make_archive(TmpDir+"/02", 'zip', root_dir=TmpDir+"/02")
    shutil.make_archive(TmpDir+"/"+basename_without_ext, 'zip', root_dir=TmpDir+"/"+basename_without_ext)
    print('アーカイブ終了')


    #アーカイブ元削除
    shutil.rmtree(TmpDir+"/"+basename_without_ext)
    print('アーカイブ元Tmpファイル削除')

print('全て終了')

sys.exit()

