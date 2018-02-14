# Python Script, API Version = V16

# Küre Oluştur
SphereBody.Create(Point.Create(MM(0), MM(0), MM(0)), Point.Create(MM(9), MM(0), MM(-21)), ExtrudeType.None)
# EndBlock

# Change Section View
result = ViewHelper.SetViewMode(InteractionMode.Solid)
# EndBlock

# Cisimleri örgülere dönüştür (Cismi meshleyebilmek için örgüye dönüştürüyoruz)
selection = Selection.Create(Body1)
result = FacetConvert.Create(selection)
# EndBlock


# Örgüyü indirge (Örgü miktarı çok fazla olduğu için indirgeme yapıyoruz. Voronoi yapınızdaki hücre sayısına göre değeri değiştirebilirsiniz)
options = FacetReduceOptions()
options.TriangleReduction = 0.95
selection = Selection.Create(MeshRegion1)
result = FacetReduce.Create(selection, options)
# EndBlock

#Önemli: Kodun bu kısmı sizde çalışmayabilir, sebebi Seçim Filtresinden sadece "Kenar" modunu açtığımız için. Kenarları kopyalayıp ana parçayı pasifleştiriyoruz)
# Copy to Clipboard
result = Copy.ToClipboard(Selection.Create(Edge1, Edge2, Edge3, Edge4, Edge5, Edge6, Edge7, Edge8, Edge9, Edge10, Edge11, Edge12, Edge13, Edge14, Edge15, Edge16, Edge17, Edge18, Edge19, Edge20, Edge21, Edge22, Edge23, Edge24, Edge25, Edge26, Edge27, Edge28, Edge29, Edge30, Edge31, Edge32, Edge33, Edge34, Edge35, Edge36, Edge37, Edge38, Edge39, Edge40, Edge41, Edge42, Edge43, Edge44, Edge45, Edge46, Edge47, Edge48, Edge49, Edge50, Edge51, Edge52, Edge53, Edge54, Edge55, Edge56, Edge57, Edge58, Edge59, Edge60, Edge61, Edge62, Edge63, Edge64, Edge65, Edge66, Edge67, Edge68, Edge69, Edge70, Edge71, Edge72, Edge73, Edge74, Edge75, Edge76, Edge77, Edge78, Edge79, Edge80, Edge81, Edge82, Edge83, Edge84, Edge85, Edge86, Edge87, Edge88, Edge89, Edge90, Edge91, Edge92, Edge93, Edge94, Edge95, Edge96, Edge97, Edge98, Edge99, Edge100, Edge101, Edge102, Edge103, Edge104, Edge105, Edge106, Edge107, Edge108, Edge109, Edge110, Edge111, Edge112, Edge113, Edge114, Edge115, Edge116, Edge117, Edge118, Edge119, Edge120, Edge121, Edge122, Edge123, Edge124, Edge125, Edge126, Edge127, Edge128, Edge129, Edge130, Edge131, Edge132, Edge133, Edge134, Edge135, Edge136, Edge137, Edge138, Edge139, Edge140, Edge141))
# EndBlock

# Panodan Yapıştır
result = Paste.FromClipboard()
# EndBlock

# Nesne Görünürlüğünü Değiştir (Ana parçayı pasifleştirdik yada gizledik)
selection = Selection.Create(Body2)
vType = VisibilityType.Hide
ViewHelper.SetObjectVisibility(selection, vType)
# EndBlock

# Taslak Silindir Oluştur(Ctrl+A ile bütün kenarları seçiyoruz, ardından otomatik silindir oluşturma ile çubuklarımızı oluşturuoruz.)
selection = Selection.Create(Curve1, Curve2, Curve3, Curve4, Curve5, Curve6, Curve7, Curve8, Curve9, Curve10, Curve11, Curve12, Curve13, Curve14, Curve15, Curve16, Curve17, Curve18, Curve19, Curve20, Curve21, Curve22, Curve23, Curve24, Curve25, Curve26, Curve27, Curve28, Curve29, Curve30, Curve31, Curve32, Curve33, Curve34, Curve35, Curve36, Curve37, Curve38, Curve39, Curve40, Curve41, Curve42, Curve43, Curve44, Curve45, Curve46, Curve47, Curve48, Curve49, Curve50, Curve51, Curve52, Curve53, Curve54, Curve55, Curve56, Curve57, Curve58, Curve59, Curve60, Curve61, Curve62, Curve63, Curve64, Curve65, Curve66, Curve67, Curve68, Curve69, Curve70, Curve71, Curve72, Curve73, Curve74, Curve75, Curve76, Curve77, Curve78, Curve79, Curve80, Curve81, Curve82, Curve83, Curve84, Curve85, Curve86, Curve87, Curve88, Curve89, Curve90, Curve91, Curve92, Curve93, Curve94, Curve95, Curve96, Curve97, Curve98, Curve99, Curve100, Curve101, Curve102, Curve103, Curve104, Curve105, Curve106, Curve107, Curve108, Curve109, Curve110, Curve111, Curve112, Curve113, Curve114, Curve115, Curve116, Curve117, Curve118, Curve119, Curve120, Curve121, Curve122, Curve123, Curve124, Curve125, Curve126, Curve127, Curve128, Curve129, Curve130, Curve131, Curve132, Curve133, Curve134, Curve135, Curve136, Curve137, Curve138, Curve139, Curve140, Curve141)
TubeBody.Create(selection, MM(0.204343221586521), ExtrudeType.None)
# EndBlock

# Cisimleri örgülere dönüştür (Çubukları tekrar meshliyoruz.)
selection = Selection.Create(GetRootPart())
result = FacetConvert.Create(selection)
# EndBlock

# Düzgün Örgü (Örgüyü birkaç kere düzelterek "Smooth" işlemine yapmaya çalışıypruz. Açı eşik değerini değiştirerek farkı görebilirisiniz.)
selection = Selection.Create(MeshRegion3)
result = FacetSmooth.Create(selection)
# EndBlock

# Düzgün Örgü
selection = Selection.Create(MeshRegion3)
result = FacetSmooth.Create(selection)
# EndBlock

# Düzgün Örgü
selection = Selection.Create(GetRootPart().Meshes[0].GetRegion([ (0, 87831)]))
result = FacetSmooth.Create(selection)
# EndBlock

# Düzgün Örgü
selection = Selection.Create(GetRootPart().Meshes[0].GetRegion([ (0, 351327)]))
result = FacetSmooth.Create(selection)
# EndBlock

