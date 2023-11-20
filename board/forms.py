from logging import PlaceHolder
from tabnanny import check
from django import forms
from .models import Qna,Notice,Review
from django_summernote.fields import SummernoteTextFormField
from django_summernote.widgets import SummernoteWidget

# qna 섬머노트
class QnAWriteForm(forms.ModelForm):

    #필드 정의 하기
    q_title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'QnA 제목'
            }
        )
    )

    q_text = SummernoteTextFormField(label='QnA 내용')


    class Meta:
        model = Qna
        fields = [
            'q_title',
            'q_text',
        ]

        widgets = {
            'q_text' : SummernoteWidget()
        }




# 공지사항 섬머노트
class noticeWriteForm(forms.ModelForm):


    not_title = forms.CharField(
        label="제목",
        widget=forms.TextInput(
            attrs={
                'placeholder' : '공지사항 제목'
            }
        )
    )

    not_content = SummernoteTextFormField(label='공지내용')


    class Meta:
        model = Notice
        fields = [
            'not_title',
            'not_content',
            'not_checks',
        ]

        widgets = {
            'not_content' : SummernoteWidget()
        }


# 사용후기 섬머노트
class  reviewWriteForm(forms.ModelForm):

    rev_title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'placeholder' : '사용후기 제목'
            }
        )
    )

    rev_afterword = SummernoteTextFormField(label='후기내용')

    class Meta:
        model = Review
        fields = [
            'rev_title',
            'rev_afterword',
        ]

        widgets = {
            'rev_afterword' : SummernoteWidget()
        }